from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from src.book_review.models import Review


class ReviewAdmin(ModelAdmin):
    list_display = ('user', 'book_link', 'ratings', 'comments')
    search_fields = ('books__title', 'user__username')
    list_filter = ('ratings',)

    def book_link(self, obj):
        url = reverse('admin:books_book_change', args=[obj.books_id])
        return format_html(f'<a href="{url}">{obj.books.title}</a>')


admin.site.register(Review, ReviewAdmin)
