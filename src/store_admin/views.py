from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from src.books.choices import GenreChoices, LanguageChoices
from src.books.models import Author, Book, Publisher
from src.core.mixins import SuperuserRequiredMixin

from .forms import BookCreateForm


class AdminDashboard(TemplateView):
    template_name = 'store_admin/dashboard.html'


class BooksList(SuperuserRequiredMixin, ListView):
    model = Book
    template_name = 'store_admin/books.html'
    paginate_by = 20


class BooksCreate(SuperuserRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'store_admin/book-create.html'
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


class BooksUpdate(SuperuserRequiredMixin, UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'store_admin/book-update.html'
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
