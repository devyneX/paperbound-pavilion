from django.contrib import admin

from .models import Order, OrderBook, Transaction


class OrderBookInline(admin.TabularInline):
    model = OrderBook
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'status', 'total_price')
    search_fields = (
        'user__username', 'address__house', 'address__street', 'address__city',
        'address__state', 'address__country', 'address__post_code'
    )
    list_filter = ('status',)
    inlines = [OrderBookInline]

    # def get

    def address(self, obj):
        return obj.address

    def total_price(self, obj):
        return obj.total_price()

    total_price.short_description = 'Total Price'  # type: ignore


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderBook)
admin.site.register(Transaction)
