from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client = Client()

    def test_login_view_ok(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get("/system/dashboard/")

        self.assertEqual(response.status_code, 200)

    def test_protected_view_redirect(self):
        response = self.client.get("/system/dashboard/")
        self.assertEqual(response.status_code, 302)
