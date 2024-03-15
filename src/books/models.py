from django.core.validators import MinValueValidator
from django.db import models

from src.core.models import BaseModel

from .choices import GenreChoices, LanguageChoices


class Author(BaseModel):
    name = models.CharField(max_length=255)

    # image = models.ImageField(
    #     upload_to='authors/images/', null=True, blank=True
    # )

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
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    language = models.CharField(max_length=3, choices=LanguageChoices)
    genre = models.CharField(max_length=20, choices=GenreChoices.choices)
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
