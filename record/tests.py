from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from record.models import Customer, Professional, Service


User = get_user_model()


class CustomerTestCase(TestCase):
    def setUp(self):
        self.customer_test = {
            "name": "Test Customer",
            "email": "test@test.com",
        }
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client = Client()
        self.client.force_login(self.user)
        self.client.post(
            "/record/customers/new/",
            {**self.customer_test},
        )

    def test_create_customer(self):
        name = "John Doe"
        email = "john@mail.com"
        self.client.post(
            "/record/customers/new/",
            {
                "name": name,
                "email": email,
            },
        )

        response = self.client.get("/record/customers/2/edit/")
        self.assertContains(response, name)

    def test_edit_customer(self):
        new_name = "Updated Customer"
        self.client.post(
            "/record/customers/1/edit/",
            {
                "name": new_name,
                "email": self.customer_test["email"],
            },
        )

        response = self.client.get("/record/customers/1/edit/")
        self.assertContains(response, new_name)

    def test_delete_customer(self):
        self.client.post("/record/customers/1/delete/")

        response = self.client.get(
            "/record/customers/",
            query_params={"ordering": "id"},
        )
        self.assertNotContains(response, self.customer_test["name"])

    def test_email_is_unique(self):
        response = self.client.post(
            "/record/customers/new/",
            {**self.customer_test},
        )
        self.assertFormError(
            response,
            "form",
            "email",
            "Customer with this Email already exists.",
        )
