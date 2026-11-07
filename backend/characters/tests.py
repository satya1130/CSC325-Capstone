
from django.test import TestCase
from django.core.management import call_command
from django.contrib import admin
from io import StringIO
from .models import Character


class CharacterAPITests(TestCase):

    def setUp(self):
        self.character = Character.objects.create(
            name="Iron Man",
            description="Smart inventor who battles in tough armor.",
            powers="Powered suit, flight, and repulsor blasts."
        )

    def test_character_list(self):
        response = self.client.get("/api/characters/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["characters"]), 1)
        self.assertEqual(
            response.json()["characters"][0]["name"],
            "Iron Man"
        )

    def test_character_detail(self):
        response = self.client.get(
            f"/api/characters/{self.character.id}/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Iron Man")

    def test_character_not_found(self):
        response = self.client.get("/api/characters/99999/")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["error"]["code"],
            "character_not_found"
        )

    def test_character_list_rejects_post(self):
        response = self.client.post("/api/characters/")

        self.assertEqual(response.status_code, 405)

    def test_character_detail_rejects_post(self):
        response = self.client.post(
            f"/api/characters/{self.character.id}/"
        )

        self.assertEqual(response.status_code, 405)

    def test_homepage(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "characters/index.html"
        )

    def test_empty_character_list(self):
        Character.objects.all().delete()
        response = self.client.get("/api/characters/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"characters": []})

    def test_unreviewed_fields_are_null(self):
        response = self.client.get(f"/api/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json()["image_ref"])
        self.assertIsNone(response.json()["category"])

    def test_import_is_idempotent(self):
        output = StringIO()
        call_command("import_characters", stdout=output)
        self.assertEqual(Character.objects.count(), 49)
        first_id = Character.objects.get(name="Iron Man").id

        # Running the importer again updates existing characters, not duplicates.
        call_command("import_characters", stdout=StringIO())
        self.assertEqual(Character.objects.count(), 49)
        self.assertEqual(Character.objects.get(name="Iron Man").id, first_id)

    def test_character_registered_with_admin(self):
        self.assertIn(Character, admin.site._registry)

    def test_us03_name_filter(self):
        Character.objects.create(name="Thor", description="Thunder", powers="Lightning")
        response = self.client.get("/api/characters/", {"q": "IRON"})
        self.assertEqual([c["name"] for c in response.json()["characters"]], ["Iron Man"])

    def test_us03_powers_filter(self):
        Character.objects.create(name="Thor", description="Thunder", powers="Lightning")
        response = self.client.get("/api/characters/", {"powers": "REPULSOR"})
        self.assertEqual([c["name"] for c in response.json()["characters"]], ["Iron Man"])

    def test_us03_combined_filters_and_empty_results(self):
        self.character.category = "Hero"
        self.character.save()
        Character.objects.create(name="Thor", description="Thunder", powers="Lightning", category="Hero")
        response = self.client.get("/api/characters/", {"q": "iron", "powers": "repulsor", "category": "hero"})
        self.assertEqual([c["name"] for c in response.json()["characters"]], ["Iron Man"])
        response = self.client.get("/api/characters/", {"q": "iron", "powers": "lightning"})
        self.assertEqual(response.json(), {"characters": []})

    def test_us03_reset_and_missing_categories(self):
        Character.objects.create(name="Thor", description="Thunder", powers="Lightning", category="Hero")
        response = self.client.get("/api/characters/", {"q": "", "powers": "", "category": ""})
        self.assertEqual(len(response.json()["characters"]), 2)
        response = self.client.get("/api/characters/", {"category": "hero"})
        self.assertEqual([c["name"] for c in response.json()["characters"]], ["Thor"])

    def test_us03_imports_all_49_character_categories(self):
        call_command("import_characters", stdout=StringIO())
        self.assertEqual(Character.objects.count(), 49)
        self.assertEqual(
            Character.objects.filter(category="Hero").count(), 36
        )
        self.assertEqual(
            Character.objects.filter(category="Villain").count(), 6
        )
        self.assertEqual(
            Character.objects.filter(category="Antihero").count(), 7
        )

    def test_us03_dropdown_has_all_character_types(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="category-filter"')
        for value in ("Hero", "Villain", "Antihero"):
            self.assertContains(response, f'<option value="{value}">')

    def test_us03_filter_imported_heroes_villains_and_antiheroes(self):
        call_command("import_characters", stdout=StringIO())
        expected = {
            "Hero": "Iron Man",
            "Villain": "Hela",
            "Antihero": "Deadpool",
        }
        for category, expected_character in expected.items():
            response = self.client.get("/api/characters/", {"category": category})
            self.assertEqual(response.status_code, 200)
            names = [character["name"] for character in response.json()["characters"]]
            self.assertIn(expected_character, names)
            self.assertTrue(all(character["category"] == category
                                for character in response.json()["characters"]))

    def test_us03_reimport_preserves_category_values(self):
        call_command("import_characters", stdout=StringIO())
        call_command("import_characters", stdout=StringIO())
        self.assertEqual(Character.objects.count(), 49)
        self.assertEqual(Character.objects.get(name="Hela").category, "Villain")
        self.assertEqual(Character.objects.get(name="Deadpool").category, "Antihero")

