from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from src.accounts.models import Address, Customer, Staff


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'username', 'email', 'phone', 'is_active',
        'address_count_link', 'order_count_link', 'review_count_link'
    )
    list_display_links = ('name', 'username')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_active',)
    inlines = [AddressInline]

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (
            'Personal info', {
                'fields': ('first_name', 'last_name', 'email', 'phone')
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['last_login', 'date_joined']
        if obj:
            return readonly_fields + ['password']

        return readonly_fields

    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(is_staff=False)
        queryset = queryset.annotate(
            address_count=models.Count('address', distinct=True),
            order_count=models.Count('order', distinct=True),
            review_count=models.Count('review', distinct=True)
        )

        return queryset

    def address_count_link(self, obj):
        url = reverse('admin:accounts_address_changelist') + '?' + urlencode({
            'user__id': obj.id
        })
        return format_html('<a href="{}">{}</a>', url, obj.address_count)

    address_count_link.short_description = 'Addresses'  # type: ignore
    address_count_link.admin_order_field = 'address_count'  # type: ignore

    def order_count_link(self, obj):
        url = reverse('admin:shopping_order_changelist') + '?' + urlencode({
            'user__id': obj.id
        })
        return format_html('<a href="{}">{}</a>', url, obj.order_count)

    order_count_link.short_description = 'Orders'  # type: ignore
    order_count_link.admin_order_field = 'order_count'  # type: ignore

    def review_count_link(self, obj):
        url = reverse('admin:book_review_review_changelist') + '?' + urlencode(
            {'user__id': obj.id}
        )
        return format_html('<a href="{}">{}</a>', url, obj.review_count)

    review_count_link.short_description = 'Reviews'  # type: ignore
    review_count_link.admin_order_field = 'review_count'  # type: ignore

    def name(self, obj):
        return f'{obj.last_name}, {obj.first_name}'

    name.admin_order_field = 'last_name'  # type: ignore

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            obj.set_password(obj.password)
            obj.save()


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'is_active')
    list_display_links = ('name', 'username')
    search_fields = ('username', 'email', 'phone', 'groups__name')
    list_filter = (
        'is_active',
        'groups',
    )

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )
        }),
        (
            'Personal info', {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'phone',
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['last_login', 'date_joined']
        if obj:
            return readonly_fields + ['password']

        return readonly_fields

    def get_queryset(self, request):
        queryset = super().get_queryset(request).filter(is_staff=True)

        return queryset

    def name(self, obj):
        return f'{obj.last_name}, {obj.first_name}'

    name.admin_order_field = 'last_name'  # type: ignore

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            obj.set_password(obj.password)
            obj.save()


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'house', 'street', 'city', 'state', 'country', 'post_code'
    )
    search_fields = (
        'user__username', 'house', 'street', 'city', 'state', 'country',
        'post_code'
    )
    list_filter = ('country',)


# admin.site.register(User)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Address, AddressAdmin)
