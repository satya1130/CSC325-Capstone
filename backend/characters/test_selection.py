import json

from bson import ObjectId
from django.test import TestCase

from .models import Character


class CharacterSelectionTests(TestCase):
    def setUp(self):
        self.thor = Character.objects.create(name="Thor", description="God.", powers="Lightning.")
        self.hulk = Character.objects.create(name="Hulk", description="Strong.", powers="Strength.")
        self.url = "/api/selection/"

    def post(self, character_id):
        return self.client.post(self.url, data=json.dumps({"character_id": character_id}),
                                content_type="application/json")

    def test_guest_can_select_and_see_selection(self):
        self.assertEqual(self.client.get(self.url).json(), {"selected": None})
        response = self.post(str(self.thor.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["selected"]["name"], "Thor")
        self.assertEqual(self.client.get(self.url).json()["selected"]["name"], "Thor")

    def test_selection_persists_across_navigation(self):
        self.post(str(self.thor.id))
        self.client.get("/")
        self.client.get("/api/characters/")
        self.assertEqual(self.client.get(self.url).json()["selected"]["id"], str(self.thor.id))

    def test_changing_selection_replaces_previous(self):
        self.post(str(self.thor.id))
        self.assertEqual(self.post(str(self.hulk.id)).json()["selected"]["name"], "Hulk")
        self.assertEqual(self.client.get(self.url).json()["selected"]["name"], "Hulk")

    def test_removing_selection_clears_it(self):
        self.post(str(self.thor.id))
        response = self.client.delete(self.url)
        self.assertEqual(response.json(), {"selected": None})
        self.assertEqual(self.client.get(self.url).json(), {"selected": None})

    def test_invalid_and_missing_characters_are_rejected(self):
        self.assertEqual(self.post("not-an-id").status_code, 400)
        self.assertEqual(self.post(str(ObjectId())).status_code, 404)
        self.assertEqual(self.client.post(self.url, data="not json", content_type="application/json").status_code, 400)
        self.assertEqual(self.client.get(self.url).json(), {"selected": None})

    def test_roster_page_still_renders_selection_hooks(self):
        response = self.client.get("/")
        self.assertContains(response, 'id="selection-panel"')
        self.assertContains(response, 'id="select-character"')
