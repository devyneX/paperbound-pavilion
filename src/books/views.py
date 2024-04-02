from django.apps import apps
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from src.core.mixins import CachedViewMixin

from .choices import GenreChoices, LanguageChoices
from .models import Author, Book, Publisher
from .view_helpers import books_general_search, books_search

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
        books = None
        search_type = request.GET.get('search_type')

        if search_type == 'general':
            books = books_general_search(request)
        else:
            books = books_search(request)

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
