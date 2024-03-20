from django.db.models import Avg, Count
from django.shortcuts import redirect
from django.views.generic import TemplateView

from src.book_review.models import Review
from src.books.models import Book
from src.core.mixins import CachedViewMixin


class UserHomeView(CachedViewMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch latest books
        latest_books = Book.objects.order_by('-created_at')[:10]
        context['latest_books'] = latest_books

        # Calculate popularity based on the number of reviews
        most_popular_books = Book.objects.annotate(
            num_reviews=Count('review')
        ).order_by('-num_reviews')[:10]
        context['most_popular_books'] = most_popular_books

        # Calculate average rating for each book
        highest_rated_books = Book.objects.annotate(
            avg_rating=Avg('review__ratings')
        ).order_by('-avg_rating')[:10]
        context['highest_rated_books'] = highest_rated_books

        # Fetch latest reviews for each book
        latest_reviews = {}
        for book in latest_books:
            reviews = Review.objects.filter(books=book
                                            ).order_by('-created_at')[:5]
            latest_reviews[book.id] = reviews
        context['latest_reviews'] = latest_reviews

        return context


def set_language(request):
    if 'language' in request.GET:
        next_url = request.META.get('HTTP_REFERER')
        lang_code = request.GET['language']
        response = redirect(next_url)
        response.set_cookie('django_language', lang_code)
        return response
    return redirect('/')
