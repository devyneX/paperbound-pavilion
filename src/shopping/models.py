from django.db import models

from accounts.models import Address, User
from books.models import Book
from src.core.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def total_price(self):
        return sum([book.price for book in self.orderbooks.all()])


class OrderBook(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderbooks',
        related_query_name='orderbook'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='orderbooks',
        related_query_name='orderbook'
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
