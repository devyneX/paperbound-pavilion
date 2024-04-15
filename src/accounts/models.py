from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from src.core.models import BaseModel


class User(AbstractUser):
    phone = models.CharField(max_length=20,
                             verbose_name=_('phone'))
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.username


class Customer(User):

    class Meta:
        proxy = True
        verbose_name = _('customer')
        verbose_name_plural = _('customers')


class Staff(User):

    class Meta:
        proxy = True
        verbose_name = _('staff')
        verbose_name_plural = _('staffs')


class Address(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='addresses',
        related_query_name='address',
        verbose_name=_('user')
    )

    house = models.CharField(verbose_name=_('house'))
    street = models.CharField(verbose_name=_('street'))
    city = models.CharField(verbose_name=_('city'))
    state = models.CharField(blank=True, null=True, verbose_name=_('state'))
    country = models.CharField(
        max_length=3,
        choices=CountryField().countries,
        verbose_name=_('country')
    )
    post_code = models.CharField(verbose_name=_('post_code'))

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return f'{self.house}, {self.street}, {self.get_country_display()}'
