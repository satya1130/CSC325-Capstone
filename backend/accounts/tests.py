from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from characters.models import Character

User = get_user_model()
PASSWORD = "Sup3r-Secret-pass"


class SignupTests(TestCase):
    def test_successful_signup_creates_hashed_account_and_signs_in(self):
        response = self.client.post(reverse("accounts:signup"), {
            "username": "fan_one",
            "email": "fan@example.com",
            "password1": PASSWORD,
            "password2": PASSWORD,
        })
        self.assertRedirects(response, "/brawl/", fetch_redirect_response=False)
        user = User.objects.get(username="fan_one")
        self.assertEqual(user.email, "fan@example.com")
        self.assertTrue(user.check_password(PASSWORD))
        self.assertNotEqual(user.password, PASSWORD)
        self.assertEqual(self.client.get("/brawl/").status_code, 200)

    def test_duplicate_username_is_rejected(self):
        User.objects.create_user("taken", "a@example.com", PASSWORD)
        response = self.client.post(reverse("accounts:signup"), {
            "username": "taken",
            "email": "b@example.com",
            "password1": PASSWORD,
            "password2": PASSWORD,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "already exists")
        self.assertEqual(User.objects.filter(username="taken").count(), 1)

    def test_duplicate_email_is_rejected(self):
        User.objects.create_user("first", "same@example.com", PASSWORD)
        response = self.client.post(reverse("accounts:signup"), {
            "username": "second",
            "email": "SAME@example.com",
            "password1": PASSWORD,
            "password2": PASSWORD,
        })
        self.assertContains(response, "email already exists")
        self.assertFalse(User.objects.filter(username="second").exists())

    def test_invalid_registration_shows_validation_errors(self):
        response = self.client.post(reverse("accounts:signup"), {
            "username": "bad",
            "email": "not-an-email",
            "password1": "123",
            "password2": "456",
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="bad").exists())
        self.assertContains(response, "Enter a valid email address")
        self.assertContains(response, "password")


class LoginLogoutTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("member", "m@example.com", PASSWORD)

    def test_successful_login_redirects_to_brawl(self):
        response = self.client.post(reverse("accounts:login"), {
            "username": "member", "password": PASSWORD,
        })
        self.assertRedirects(response, "/brawl/", fetch_redirect_response=False)

    def test_login_honours_safe_next_parameter(self):
        response = self.client.post(
            reverse("accounts:login") + "?next=/brawl/",
            {"username": "member", "password": PASSWORD, "next": "/brawl/"},
        )
        self.assertRedirects(response, "/brawl/", fetch_redirect_response=False)

    def test_unsafe_next_parameter_is_ignored(self):
        response = self.client.post(
            reverse("accounts:login") + "?next=https://evil.example/",
            {"username": "member", "password": PASSWORD, "next": "https://evil.example/"},
        )
        self.assertRedirects(response, "/brawl/", fetch_redirect_response=False)

    def test_incorrect_credentials_are_rejected(self):
        response = self.client.post(reverse("accounts:login"), {
            "username": "member", "password": "wrong-password",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_session_persists_across_permitted_visits(self):
        self.client.force_login(self.user)
        for _ in range(3):
            self.assertEqual(self.client.get("/").status_code, 200)
            self.assertEqual(self.client.get("/brawl/").status_code, 200)
        self.assertContains(self.client.get("/"), "Signed in as")
        self.assertContains(self.client.get("/"), "member")

    def test_logout_invalidates_session(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get("/brawl/").status_code, 200)
        response = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(response, "/", fetch_redirect_response=False)
        self.assertNotIn("_auth_user_id", self.client.session)
        response = self.client.get("/brawl/")
        self.assertRedirects(response, "/accounts/login/?next=/brawl/", fetch_redirect_response=False)

    def test_logout_requires_post(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(reverse("accounts:logout")).status_code, 405)
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_redirect_target_for_brawl_guest(self):
        response = self.client.get("/brawl/")
        self.assertRedirects(response, "/accounts/login/?next=/brawl/", fetch_redirect_response=False)


class PermissionTests(TestCase):
    def setUp(self):
        self.member = User.objects.create_user("member", "m@example.com", PASSWORD)
        self.admin = User.objects.create_user("admin", "a@example.com", PASSWORD, is_staff=True)
        self.character = Character.objects.create(
            name="Thor", description="God of thunder.", powers="Lightning. Strength.",
        )

    def test_guests_browse_public_roster_and_profiles(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        self.assertEqual(self.client.get("/api/characters/").status_code, 200)
        url = f"/api/characters/{self.character.id}/"
        self.assertEqual(self.client.get(url).status_code, 200)

    def test_guest_denied_brawl_page_and_api(self):
        self.assertEqual(self.client.get("/brawl/").status_code, 302)
        response = self.client.post("/api/brawl/start/", data="{}", content_type="application/json")
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_member_can_access_brawl_arena(self):
        self.client.force_login(self.member)
        self.assertEqual(self.client.get("/brawl/").status_code, 200)

    def test_guest_and_member_cannot_reach_admin_control_room(self):
        response = self.client.get(reverse("accounts:admin_control"))
        self.assertRedirects(
            response, "/accounts/login/?next=/accounts/admin-control/", fetch_redirect_response=False,
        )
        self.client.force_login(self.member)
        self.assertEqual(self.client.get(reverse("accounts:admin_control")).status_code, 403)

    def test_authorized_admin_can_reach_admin_control_room(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse("accounts:admin_control"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Control Room")

    def test_guests_and_members_cannot_modify_protected_roster_content(self):
        payload = '{"name": "Hacked", "description": "x", "powers": "y"}'
        for client_user in (None, self.member):
            if client_user:
                self.client.force_login(client_user)
            else:
                self.client.logout()
            response = self.client.post("/api/characters/", data=payload, content_type="application/json")
            self.assertEqual(response.status_code, 405)
        self.assertFalse(Character.objects.filter(name="Hacked").exists())
