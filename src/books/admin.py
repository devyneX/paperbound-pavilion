from django.contrib import admin

from .models import Author, Book, Publisher

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
