from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from unfold.admin import ModelAdmin, StackedInline

from src.books.models import Author, Book, Publisher


class BookAdmin(ModelAdmin):
    list_display = (
        'title', 'author_link', 'publisher_link', 'price', 'quantity',
        'review_count_link'
    )
    search_fields = ('title', 'author__name', 'publisher__name')
    list_filter = ('author', 'publisher', 'language', 'genre')

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'publisher')
        }),
        ('Details', {
            'fields': ('language', 'genre', 'price', 'quantity')
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            review_count=models.Count('review', distinct=True)
        )

        return queryset

    def author_link(self, obj):
        url = reverse('admin:books_author_change', args=[obj.author_id])
        return format_html(f'<a href="{url}">{obj.author.name}</a>')

    author_link.short_description = 'Author'  # type: ignore
    author_link.admin_order_field = 'author__name'  # type: ignore

    def publisher_link(self, obj):
        url = reverse('admin:books_publisher_change', args=[obj.publisher_id])
        return format_html(f'<a href="{url}">{obj.publisher.name}</a>')

    publisher_link.short_description = 'Publisher'  # type: ignore
    publisher_link.admin_order_field = 'publisher__name'  # type: ignore

    def review_count_link(self, obj):
        url = reverse('admin:book_review_review_changelist') + '?' + urlencode(
            {'books__id': obj.id}
        )
        return format_html('<a href="{}">{}</a>', url, obj.review_count)

    review_count_link.short_description = 'Reviews'  # type: ignore
    review_count_link.admin_order_field = 'review_count'  # type: ignore


class BookInline(StackedInline):
    model = Book
    extra = 1


class AuthorAdmin(ModelAdmin):
    list_display = ('name', 'book_count_link')
    inlines = [BookInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(book_count=models.Count('book'))

        return queryset

    def book_count_link(self, obj):
        count = obj.book_count
        url = (
            reverse('admin:books_book_changelist') + '?' +
            urlencode({'author__id': f'{obj.id}'})
        )

        return format_html(f'<a href="{url}">{count}</a>')

    book_count_link.short_description = 'Books'  # type: ignore
    book_count_link.admin_order_field = 'book_count'  # type: ignore


class PublisherAdmin(ModelAdmin):
    list_display = ('name', 'address', 'book_count_link')
    inlines = [BookInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(book_count=models.Count('book'))

        return queryset

    def book_count_link(self, obj):
        count = obj.book_count
        url = (
            reverse('admin:books_book_changelist') + '?' +
            urlencode({'publisher__id': f'{obj.id}'})
        )

        return format_html(f'<a href="{url}">{count}</a>')

    book_count_link.short_description = 'Books'  # type: ignore
    book_count_link.admin_order_field = 'book_count'  # type: ignore


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
