from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=False, null=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_seller = models.BooleanField(null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomUserManager()
