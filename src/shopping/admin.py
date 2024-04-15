from django.contrib import admin
from django.db import models
from django.urls import path, reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Order, OrderBook, Transaction


class OrderBookInline(admin.TabularInline):
    model = OrderBook
    extra = 1


class TransactionInline(admin.StackedInline):
    model = Transaction
    extra = 0
    readonly_fields = [
        'transaction_id', 'created_at', 'updated_at', 'status', 'amount',
        'currency', 'bank_tran_id', 'store_amount'
    ]


class OrderAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        'user', 'created_at', 'address_link', 'status', 'total_price',
        'orderitem_count_link'
    )
    search_fields = (
        'user__username', 'address__house', 'address__street', 'address__city',
        'address__state', 'address__country', 'address__post_code'
    )
    list_filter = ('status',)
    actions = ['update_status']
    inlines = [TransactionInline, OrderBookInline]

    fieldsets = (
        (None, {
            'fields': ('user', 'address', 'status')
        }),
        ('Details', {
            'fields': ('total_price', 'created_at', 'updated_at')
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request).prefetch_related('address')
        queryset = queryset.annotate(
            orderitem_count=models.Count('orderbook', distinct=True)
        ).order_by('created_at')

        return queryset

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['created_at', 'updated_at', 'total_price']

        return readonly_fields

    def address(self, obj):
        return obj.address

    def total_price(self, obj):
        return obj.total_price()

    total_price.short_description = 'Total Price'  # type: ignore
    total_price.admin_order_field = 'total_price'  # type: ignore

    def orderitem_count_link(self, obj):
        url = reverse('admin:shopping_orderbook_changelist') + '?' + urlencode(
            {'order__id': obj.id}
        )
        return format_html('<a href="{}">{}</a>', url, obj.orderitem_count)

    orderitem_count_link.short_description = 'Order Items'  # type: ignore
    orderitem_count_link.admin_order_field = 'orderitem_count'  # type: ignore

    def address_link(self, obj):
        url = reverse('admin:accounts_address_change', args=[obj.address_id])
        return format_html(f'<a href="{url}">{obj.address}</a>')

    address_link.short_description = 'Address'  # type: ignore
    address_link.admin_order_field = 'address__house'  # type: ignore

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('update-status/', self.update_status, name='update_status')
        ]

        return custom_urls + urls

    def update_status(self, request, queryset):
        for order in queryset:
            order.status = order.get_next_status()
            order.save()

        self.message_user(request, 'Order status updated successfully')


class OrderBookAdmin(admin.ModelAdmin):
    list_display = ('order', 'book_link', 'quantity', 'price')
    search_fields = ('order__user__username', 'book__title')
    list_filter = ('order__status',)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['total_price']

        return readonly_fields

    def book_link(self, obj):
        url = reverse('admin:books_book_change', args=[obj.book_id])
        return format_html(f'<a href="{url}">{obj.book.title}</a>')

    book_link.short_description = 'Book'  # type: ignore
    book_link.admin_order_field = 'book__title'  # type: ignore


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'transaction_id', 'order_link', 'status', 'amount', 'store_amount',
        'currency'
    )
    search_fields = ('order__user__username', 'transaction_id')
    list_filter = ('status', 'currency')
    readonly_fields = [
        'transaction_id', 'created_at', 'updated_at', 'status', 'amount',
        'currency', 'bank_tran_id', 'store_amount', 'order_link'
    ]

    def order_link(self, obj):
        url = reverse('admin:shopping_order_change', args=[obj.order_id])
        return format_html(f'<a href="{url}">{obj.order}</a>')

    order_link.short_description = 'Order'  # type: ignore
    order_link.admin_order_field = 'order__created_at'  # type: ignore


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderBook, OrderBookAdmin)
admin.site.register(Transaction, TransactionAdmin)
