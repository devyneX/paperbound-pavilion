from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.books.choices import GenreChoices, LanguageChoices
from src.books.models import Author, Book, Publisher

from ..forms import BookCreateForm


# BOOK VIEWS
class BooksList(PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'store_admin/book/books.html'
    paginate_by = 20
    permission_required = ('books.view_book',)


class BooksCreate(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'store_admin/book/book-create.html'
    success_url = reverse_lazy('admin-books')
    permission_required = ('books.add_book',)

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


class BookDetailView(PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'store_admin/book/book-detail.html'
    permission_required = ('books.view_book',)


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy(
        'admin-books'
    )  # Redirect to admin users list after deletion
    template_name = 'store_admin/book/book-confirm-delete.html'
    permission_required = ('books.delete_book',)


class BooksUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'store_admin/book/book-update.html'
    success_url = reverse_lazy('admin-books')
    permission_required = ('books.change_book',)

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
