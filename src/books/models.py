from django.db import models
from languages.fields import LanguageField

from core.models import BaseModel

from .utils import GenreChoices


class Author(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='authors/images/', null=True, blank=True
    )

    def __str__(self):
        return self.name

    # def total_books(self):
    #     return self.books.coun


class Publisher(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

    # def total_books(self):
    #     return self.books.count()


class Book(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    language = LanguageField()
    genre = models.CharField(max_length=20, choices=GenreChoices.choices)
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        related_query_name='book'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
        related_query_name='book'
    )

    def __str__(self):
        return f'{self.title} by {self.author.name}'
