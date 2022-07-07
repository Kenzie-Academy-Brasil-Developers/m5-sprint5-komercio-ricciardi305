from rest_framework.test import APITestCase
from ..models import User
from ..serializers import UserSerializer


class UsersViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "rafael@mail.com"
        cls.password = "1234"
        cls.first_name = "Rafael"
        cls.last_name = "Ricciardi"

        cls.seller = User.objects.create(
            email=cls.email,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=True,
        )

        cls.buyer = User.objects.create(
            email="rafael2@mail.com",
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=False,
        )

    def test_can_create_a_seller(self):
        user = {
            "email": "rafael1@mail.com",
            "password": "1234",
            "first_name": "Rafael",
            "last_name": "Ricciardi",
            "is_seller": True,
        }
        response = self.client.post(
            "/api/accounts/",
            user,
        )
        self.assertEquals(response.status_code, 201)

    def test_can_create_a_buyer(self):
        user = {
            "email": "rafael11@mail.com",
            "password": "1234",
            "first_name": "Rafael",
            "last_name": "Ricciardi",
            "is_seller": False,
        }
        response = self.client.post(
            "/api/accounts/",
            user,
        )
        self.assertEquals(response.status_code, 201)

    def test_cannot_create_a_seller_with_invalid_keys(self):
        user = {
            "email": "rafael@mail.com",
            "password": "1234",
            "first_name": "Rafael",
            "last_name": "Ricciardi",
            "is_seller": True,
        }

        response = self.client.post(
            "/api/accounts/",
            user,
        )
        self.assertEquals(response.status_code, 400)

    def test_cannot_create_a_buyer_with_invalid_keys(self):
        user = {
            "email": "rafael23@mail.com",
            "password": "1234",
            "is_seller": False,
        }

        response = self.client.post(
            "/api/accounts/",
            user,
        )
        self.assertEquals(response.status_code, 400)

    def test_login_seller(self):
        user = User.objects.create(
            email="loginseller@mail.com",
            password="abc",
            first_name="Rafael",
            last_name="Ricciardi",
            is_seller=True,
        )
        response = self.client.post("/api/login/", {"email": "rafael@mail.com", "password": "1234"})

    def test_can_list_all_users(self):
        response = self.client.get("/api/accounts/")
        self.assertEquals(response.status_code, 200)
        
        
