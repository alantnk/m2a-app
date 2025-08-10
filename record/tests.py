from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model


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
        self.assertContains(
            response,
            f"Erro: Email {self.customer_test['email']}",  # noqa: E501
        )


class ProfessionalTestCase(TestCase):
    def setUp(self):
        self.professional_test = {
            "name": "Test Professional",
            "email": "test@test.com",
        }
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client = Client()
        self.client.force_login(self.user)
        self.client.post(
            "/record/professionals/new/",
            {**self.professional_test},
        )

    def test_create_professional(self):
        name = "Jane Doe"
        email = "jane@mail.com"
        self.client.post(
            "/record/professionals/new/",
            {
                "name": name,
                "email": email,
            },
        )
        response = self.client.get("/record/professionals/2/edit/")
        self.assertContains(response, name)

    def test_edit_professional(self):
        new_name = "Updated Professional"
        self.client.post(
            "/record/professionals/1/edit/",
            {
                "name": new_name,
                "email": self.professional_test["email"],
            },
        )

        response = self.client.get("/record/professionals/1/edit/")
        self.assertContains(response, new_name)

    def test_delete_professional(self):
        self.client.post("/record/professionals/1/delete/")

        response = self.client.get(
            "/record/professionals/",
            query_params={"ordering": "id"},
        )
        self.assertNotContains(response, self.professional_test["name"])

    def test_email_is_unique(self):
        response = self.client.post(
            "/record/professionals/new/",
            {**self.professional_test},
        )
        self.assertContains(
            response,
            f"Erro: Email {self.professional_test['email']}",  # noqa: E501
        )


class ServiceTestCase(TestCase):
    def setUp(self):
        self.service_test = {"title": "Test Service"}
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.client = Client()
        self.client.force_login(self.user)
        self.client.post(
            "/record/services/new/",
            {**self.service_test},
        )

    def test_create_service(self):
        title = "New Service"
        self.client.post(
            "/record/services/new/",
            {
                "title": title,
            },
        )
        response = self.client.get("/record/services/2/edit/")
        self.assertContains(response, title)

    def test_edit_service(self):
        new_title = "Updated Service"
        self.client.post(
            "/record/services/1/edit/",
            {
                "title": new_title,
            },
        )

        response = self.client.get("/record/services/1/edit/")
        self.assertContains(response, new_title)

    def test_delete_service(self):
        self.client.post("/record/services/1/delete/")

        response = self.client.get(
            "/record/services/",
            query_params={"ordering": "id"},
        )
        self.assertNotContains(response, self.service_test["title"])

    def test_service_title_is_unique(self):
        response = self.client.post(
            "/record/services/new/",
            {**self.service_test},
        )
        self.assertContains(
            response,
            "Erro: Já existe um serviço com esse nome.",  # noqa: E501
        )
