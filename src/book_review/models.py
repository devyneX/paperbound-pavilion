from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from src.accounts.models import User
from src.books.models import Book
from src.core.models import BaseModel


class Review(BaseModel):
    ratings = models.IntegerField(
        validators=[MaxValueValidator(5),
                    MinValueValidator(1)]
    )
    comments = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        related_query_name='review'
    )
    books = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
        related_query_name='review'
    )
