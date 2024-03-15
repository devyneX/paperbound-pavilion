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
    state = models.CharField(blank=True, null=True)
    country = models.CharField(
        max_length=200, null=True, choices=CountryField().choices
    )
    post_code = models.CharField()

    def __str__(self):
        return f'{self.house}, {self.street}, {self.get_country_display()}'
