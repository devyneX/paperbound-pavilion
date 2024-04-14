from django.contrib import admin

from src.book_review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'books', 'ratings', 'comments')
    search_fields = ('books__title', 'user__username')
    list_filter = ('ratings',)

    def books(self, obj):
        return obj.book.title

    def user(self, obj):
        return obj.user.username


admin.site.register(Review, ReviewAdmin)
