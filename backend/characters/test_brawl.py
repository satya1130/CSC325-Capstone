"""Epic 5: pure engine tests and Django API integration tests."""
import json
from bson import ObjectId
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from .brawl import InvalidMatchup, simulate
from .models import Character


class BrawlEngineTests(SimpleTestCase):
    def setUp(self):
        self.first = {"id": "a", "name": "Alpha"}
        self.second = {"id": "b", "name": "Beta"}

    def test_deterministic(self):
        self.assertEqual(simulate(self.first, self.second), simulate(self.first, self.second))

    def test_rejects_duplicate_or_missing_fighters(self):
        with self.assertRaises(InvalidMatchup):
            simulate(self.first, self.first)
        with self.assertRaises(InvalidMatchup):
            simulate(self.first, {})

    def test_health_bounds_turn_order_and_winner(self):
        result = simulate(self.first, self.second)
        self.assertTrue(result["simulation"])
        self.assertTrue(result["turns"])
        self.assertLessEqual(len(result["turns"]), 100)
        for i, turn in enumerate(result["turns"]):
            self.assertEqual(turn["turn"], i + 1)
            self.assertTrue(0 <= turn["health_after"] <= 100)
            self.assertTrue(all(0 <= hp <= 100 for hp in turn["health"]))
            self.assertTrue(1 <= turn["damage"] <= 20)
        self.assertIn(result["winner"]["id"], ("a", "b"))
        self.assertEqual(min(f["health"] for f in result["fighters"]), 0)


class BrawlAPITests(TestCase):
    def setUp(self):
        self.first = Character.objects.create(name="Alpha", description="A", powers="A")
        self.second = Character.objects.create(name="Beta", description="B", powers="B")
        self.user = get_user_model().objects.create_user(username="brawltester", password="strong-example-pass-123")

    def test_guest_requires_login(self):
        response = self.client.get("/brawl/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post("/api/brawl/start/", data=json.dumps({
            "fighter1": str(self.first.id), "fighter2": str(self.second.id)
        }), content_type="application/json")
        self.assertEqual(response.status_code, 302)

    def test_valid_match_and_page(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get("/brawl/").status_code, 200)
        response = self.client.post("/api/brawl/start/", data=json.dumps({
            "fighter1": str(self.first.id), "fighter2": str(self.second.id)
        }), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["rules_version"], "brawl_v1")
        self.assertIn(response.json()["winner"]["name"], ("Alpha", "Beta"))

    def test_rejects_same_missing_and_invalid(self):
        self.client.force_login(self.user)
        def post(a, b):
            return self.client.post("/api/brawl/start/", data=json.dumps({
                "fighter1": a, "fighter2": b
            }), content_type="application/json")
        self.assertEqual(post(str(self.first.id), str(self.first.id)).status_code, 400)
        self.assertEqual(post("", str(self.second.id)).status_code, 400)
        self.assertEqual(post(str(ObjectId()), str(self.second.id)).status_code, 404)
        self.assertEqual(post(str(self.first.id), str(self.second.id)).json()["simulation"], True)

    def test_get_not_allowed(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get("/api/brawl/start/").status_code, 405)
