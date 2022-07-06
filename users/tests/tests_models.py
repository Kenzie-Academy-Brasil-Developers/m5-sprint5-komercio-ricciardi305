from django.test import TestCase
from ..models import User
from django.db import IntegrityError

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "alexandre@mail.com"
        cls.first_name = "alexandre"
        cls.last_name = "alves",
        cls.is_seller = True

        cls.user = User.objects.create(
            email = cls.email,
            first_name = cls.first_name,
            last_name = cls.last_name,
            is_seller = cls.is_seller
        )

    def test_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("email").max_length
        self.assertEquals(max_length, 255)
    
    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("first_name").max_length
        self.assertEquals(max_length, 50)
    
    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("last_name").max_length
        self.assertEquals(max_length, 50)

    def test_email_unique(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(
                email = self.email,
                first_name = self.first_name,
                last_name = self.last_name,
                is_seller = self.is_seller
            )
    
    def test_user_has_information_fields(self):
        self.assertEquals(self.user.email, self.email)
        self.assertEquals(self.user.first_name, self.first_name)
        self.assertEquals(self.user.last_name, self.last_name)
        self.assertEquals(self.user.is_seller, self.is_seller)
        self.assertIsNone(self.user.username)
        self.assertTrue(self.user.is_active)
	    
