from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from src.core.models import BaseModel


class User(AbstractUser):
    phone = models.CharField(max_length=20)


class Address(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses'
    )

    house = models.CharField()
    street = models.CharField()
    city = models.CharField()
    state = models.CharField()
    country = CountryField()
    post_code = models.CharField()
