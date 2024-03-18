from django.db import models

from src.accounts.models import Address, User
from src.books.models import Book
from src.core.models import BaseModel


class OrderStatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    SHIPPED = 'SHIPPED', 'Shipped'
    DELIVERED = 'DELIVERED', 'Delivered'
    CANCELLED = 'CANCELLED', 'Cancelled'


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING
    )
    books = models.ManyToManyField(Book, through='OrderBook')

    def total_price(self):
        return self.orderbooks.filter(out_of_stock=False).aggregate(
            total_price=models.Sum(models.F('quantity') * models.F('price'))
        )['total_price']


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
    out_of_stock = models.BooleanField(default=False)


class PaymentStatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    SUCCESS = 'SUCCESS', 'Success'
    FAILED = 'FAILED', 'Failed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class Transaction(BaseModel):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='transaction',
        related_query_name='transaction'
    )
    transaction_id = models.CharField(max_length=50, primary_key=True)
    bank_tran_id = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    store_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    currency = models.CharField(max_length=5)
    status = models.CharField(max_length=10, choices=PaymentStatusChoices)
