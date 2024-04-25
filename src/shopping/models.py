from django.db import models
from django.utils.translation import gettext_lazy as _

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

    def next_state(self):
        if self == OrderStatusChoices.PENDING:
            return OrderStatusChoices.PROCESSING
        if self == OrderStatusChoices.PROCESSING:
            return OrderStatusChoices.CONFIRMED
        if self == OrderStatusChoices.CONFIRMED:
            return OrderStatusChoices.SHIPPED
        if self == OrderStatusChoices.SHIPPED:
            return OrderStatusChoices.DELIVERED
        return self


class Order(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name=_('user'),
                             related_name='orders',
                             related_query_name='order'
                             )
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                verbose_name=_('address'))
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
        verbose_name=_('status')
    )
    books = models.ManyToManyField(Book, through='OrderBook',
                                   verbose_name=_('books'))

    class Meta:
        permissions = (
            ('view_own_order', 'Can view own order'),
            ('place_order', 'Can place order'),
        )

    def total_price(self):
        return self.orderbooks.filter(out_of_stock=False).aggregate(
            total_price=models.Sum(models.F('quantity') * models.F('price'))
        )['total_price']

    def get_next_status(self):
        return OrderStatusChoices.next_state(self.status)

    def __str__(self) -> str:
        return f'{self.user.username} -\
            {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'


class OrderBook(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderbooks',
        related_query_name='orderbook',
        verbose_name=_('order')
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='orderbooks',
        related_query_name='orderbook',
        verbose_name=_('book')
    )
    quantity = models.IntegerField(verbose_name=_('quantity'))
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name=_('price'))
    out_of_stock = models.BooleanField(default=False,
                                       verbose_name=_('out_of_stock'))


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
        related_query_name='transaction',
    )
    transaction_id = models.CharField(max_length=50, primary_key=True)
    bank_tran_id = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    store_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    currency = models.CharField(max_length=5)
    status = models.CharField(max_length=10, choices=PaymentStatusChoices)
