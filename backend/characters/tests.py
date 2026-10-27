
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
