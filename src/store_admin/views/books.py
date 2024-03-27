from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.books.choices import GenreChoices, LanguageChoices
from src.books.models import Author, Book, Publisher
from src.core.mixins import CachedViewMixin, SuperuserRequiredMixin

from ..forms import BookCreateForm


# BOOK VIEWS
class BooksList(SuperuserRequiredMixin, CachedViewMixin, ListView):
    model = Book
    template_name = 'store_admin/book/books.html'
    paginate_by = 20


class BooksCreate(SuperuserRequiredMixin, CachedViewMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'store_admin/book/book-create.html'
    success_url = reverse_lazy('admin-books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add genre and language choices to the context
        context['genre_choices'] = GenreChoices.choices
        context['language_choices'] = LanguageChoices.choices
        # Add authors to the context
        context['authors'] = Author.objects.all()
        # Add publishers to the context
        context['publishers'] = Publisher.objects.all()
        return context


class BookDetailView(SuperuserRequiredMixin, CachedViewMixin, DetailView):
    model = Book
    template_name = 'store_admin/book/book-detail.html'


class BookDelete(SuperuserRequiredMixin, CachedViewMixin, DeleteView):
    model = Book
    success_url = reverse_lazy(
        'admin-books'
    )  # Redirect to admin users list after deletion
    template_name = 'store_admin/book/book-confirm-delete.html'


class BooksUpdate(SuperuserRequiredMixin, CachedViewMixin, UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'store_admin/book/book-update.html'
    success_url = reverse_lazy('admin-books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add genre and language choices to the context
        context['genre_choices'] = GenreChoices.choices
        context['language_choices'] = LanguageChoices.choices
        # Add authors to the context
        context['authors'] = Author.objects.all()
        # Add publishers to the context
        context['publishers'] = Publisher.objects.all()
        return context
