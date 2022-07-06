from django.test import TestCase
from ..models import Product
from users.models import User

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.description = "Smartband XYZ 3.0"
        cls.price = 100.99
        cls.quantity = 15
        cls.is_active = True

        cls.products = [Product.objects.create(
            description = cls.description,
            price = cls.price,
            quantity = cls.quantity,
            is_active = cls.is_active
            )
            for _ in range(20)
        ]

        cls.user = User.objects.create(
            email = "alexandre@mail.com",
            first_name = "alexandre",
            last_name = "alves",
            is_seller = True
        )
    
    def test_product_is_active(self):
        product = Product.objects.get(id=1)
        is_active = product._meta.get_field("is_active")
        self.assertTrue(is_active)

    def test_product_has_information_fields(self):
        self.assertEquals(self.product.description, self.description)
        self.assertEquals(self.product.price, self.price)
        self.assertEquals(self.product.quantity, self.quantity)
        self.assertEquals(self.product.is_active, self.is_active)
        self.assertIsNone(self.product.seller)

    def test_user_may_contain_multiple_products(self):
        for product in self.products:
            product.seller = self.user
            product.save()
        
        self.assertEquals(
            len(self.products),
            self.user.products.count()
        )

        for product in self.products:
            self.assertIs(product.user, self.user)

    def test_product_cannot_belong_to_more_one_user(self):
        for product in self.products:
            product.seller = self.user
            product.save()
        
        user_two = User.objects.create(
            email = "rafael@mail.com",
            first_name = "Rafael",
            last_name = "Ricciardi",
            is_seller = True
        )

        for product in self.products:
            product.seller = user_two
            product.save()

        for product in self.products:
            self.assertNotIn(product, self.user.products.all())
            self.assertIn(product, self.user_two.products.all())

    