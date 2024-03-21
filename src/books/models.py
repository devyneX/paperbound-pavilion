from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.core.models import BaseModel

from .choices import GenreChoices, LanguageChoices


class Author(BaseModel):
    name = models.CharField(max_length=255,
                            verbose_name=_('name'))

    # image = models.ImageField(
    #     upload_to='authors/images/', null=True, blank=True
    # )

    def __str__(self):
        return self.name

    # def total_books(self):
    #     return self.books.coun


class Publisher(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    address = models.TextField(verbose_name=_('address'))

    def __str__(self):
        return self.name

    # def total_books(self):
    #     return self.books.count()


class Book(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name=_('price'))
    quantity = models.IntegerField(validators=[MinValueValidator(0)],
                                   verbose_name=_('quantity'))
    language = models.CharField(max_length=3, choices=LanguageChoices,
                                verbose_name=_('language'))
    genre = models.CharField(max_length=20, choices=GenreChoices.choices,
                             verbose_name=_('genre'))
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        related_query_name='book',
        verbose_name=_('author')
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
        related_query_name='book',
        verbose_name=_('publisher')
    )

    def __str__(self):
        return f'{self.title} by {self.author.name}'
