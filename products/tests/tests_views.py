from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from users.models import User
from ..models import Product
from ..serializers import GetProductsSerialier
from django.db import IntegrityError


class ProductsViewsTest(APITestCase):
    def setUp(self) -> None:
        buyer = User.objects.create(
            email="rafael@mail.com",
            password="1234",
            first_name="Rafael",
            last_name="Ricciardi",
            is_seller=False,
        )

        seller = User.objects.create(
            email="rafael1@mail.com",
            password="1234",
            first_name="Rafael",
            last_name="Ricciardi",
            is_seller=True,
        )

        self.token_buyer = Token.objects.create(user=buyer)
        self.token_seller = Token.objects.create(user=seller)

    def test_buyer_cannot_create_a_product(self):
        product = {
            "description": "Smartband XYZ 3.0",
            "price": 100.99,
            "quantity": 15,
            "is_active": True,
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_buyer.key)
        response = self.client.post("/api/products/", product)
        self.assertEquals(response.status_code, 403)

    def test_seller_can_create_a_product(self):
        product = {
            "description": "Smartband XYZ 3.0",
            "price": 100.99,
            "quantity": 15,
            "is_active": True,
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)
        response = self.client.post("/api/products/", product)
        self.assertEquals(response.status_code, 201)

    def test_only_seller_can_update_a_product(self):
        seller = User.objects.get(id=2)
        product = Product.objects.create(
            description="Smartband XYZ 3.0",
            price=100.99,
            quantity=15,
            is_active=True,
            seller=seller,
        )
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token_seller.key)
        response = self.client.patch(f"/api/products/{product.id}/")
        self.assertEquals(response.status_code, 200)

    def test_anyone_can_list_products(self):
        seller = User.objects.get(id=2)
        products = [
            Product.objects.create(
                description="Smartband XYZ 3.0",
                price=100.99,
                quantity=15,
                is_active=True,
                seller=seller,
            )
            for product in range(10)
        ]
        response = self.client.get("/api/products/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(products), len(response.data["results"]))

        for product in products:
            self.assertIn(
                GetProductsSerialier(instance=product).data, response.data["results"]
            )

    def test_anyone_can_retrieve_a_specific_product(self):
        seller = User.objects.get(id=2)
        products = [
            Product.objects.create(
                description="Smartband XYZ 3.0",
                price=100.99,
                quantity=15,
                is_active=True,
                seller=seller,
            )
            for product in range(10)
        ]
        product = products[0]
        response = self.client.get(f"/api/products/{product.id}/")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()["id"], product.id)

        self.assertEqual(GetProductsSerialier(instance=product).data, response.data)
