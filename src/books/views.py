from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from src.core.mixins import CachedViewMixin

from .choices import GenreChoices, LanguageChoices
from .models import Author, Book, Publisher

Review = apps.get_model('book_review', 'Review')


def get_username_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        username = user.username
        return username
    except User.DoesNotExist:
        return None


class BookListView(ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'book_list'
    template_name = 'book_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        cart = self.request.session.get('cart', {})
        # annotate the queryset with the cart quantity
        for book in queryset:
            book.cart_quantity = cart.get(str(book.pk), 0)

        return queryset


class BookDetailView(CachedViewMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart = self.request.session.get('cart', {})
        context['book'].cart_quantity = cart.get(str(self.object.pk), 0)

        reviews = Review.objects.filter(books__id=self.object.pk)
        for review in reviews:
            review.range = range(review.ratings)

        context['reviews'] = reviews

        return context


class BookSearch(CachedViewMixin, View):

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()

        # Search by author name using full-text search
        author_query = request.GET.get('author')
        if author_query:
            books = books.annotate(
                author_search=SearchVector('author__name'),
            ).filter(author_search=author_query)

        # Search by book name using full-text search
        book_name_query = request.GET.get('book_name')
        if book_name_query:
            books = books.annotate(book_name_search=SearchVector('title'),
                                   ).filter(book_name_search=book_name_query)

        # Search by publisher name using full-text search
        publisher_query = request.GET.get('publisher')
        if publisher_query:
            books = books.annotate(
                publisher_search=SearchVector('publisher__name'),
            ).filter(publisher_search=publisher_query)

        # Filter by price range
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if min_price and max_price:
            books = books.filter(price__range=(min_price, max_price))

        # Filter by publication date range
        # start_date = request.GET.get('start_date')
        # end_date = request.GET.get('end_date')
        # if start_date and end_date:
        #     books = books.filter(
        #         publication_date__range=(start_date, end_date)
        #     )

        # Filter by book genre
        genre = request.GET.get('genre')
        if genre:
            books = books.filter(genre=genre)

        # Filter by book language
        language = request.GET.get('language')
        if language:
            books = books.filter(language=language)

        # Filter by publisher name
        publisher = request.GET.get('publisher')
        if publisher:
            books = books.filter(publisher__name=publisher)

        context = {}
        context['books'] = books
        context['genres'] = GenreChoices.choices
        context['languages'] = LanguageChoices.choices
        # Add authors to the context
        context['authors'] = Author.objects.all()
        # Add publishers to the context
        context['publishers'] = Publisher.objects.all()
        context['params'] = request.GET

        return render(request, 'book_search_result.html', context)
