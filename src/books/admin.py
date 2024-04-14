from django.contrib import admin
from django.db import models

from src.books.models import Author, Book, Publisher


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'price', 'quantity')
    search_fields = ('title', 'author__name', 'publisher__name')
    list_filter = ('author', 'publisher', 'language', 'genre')


class BookInline(admin.StackedInline):
    model = Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count')
    inlines = [BookInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(book_count=models.Count('book'))

        return queryset

    def book_count(self, obj):
        return obj.book_count

    book_count.admin_order_field = 'book_count'  # type: ignore


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'book_count')
    inlines = [BookInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(book_count=models.Count('book'))

        return queryset

    def book_count(self, obj):
        return obj.book_count

    book_count.admin_order_field = 'book_count'  # type: ignore


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
