import json

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from src.books.choices import GenreChoices, LanguageChoices
from src.books.models import Author, Book, Publisher
from src.core.mixins import SuperuserRequiredMixin
from src.shopping.models import Order, OrderBook

from .forms import (
    AuthorCreateForm, BookCreateForm, OrderCreateForm, PublisherCreateForm
)


class AdminDashboard(TemplateView):
    template_name = 'store_admin/dashboard.html'


# BOOK VIEWS
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


# AUTHOR VIEWS
class AuthorsList(SuperuserRequiredMixin, ListView):
    model = Author
    template_name = 'store_admin/authors.html'
    paginate_by = 20


class AuthorsCreate(SuperuserRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'store_admin/author-create.html'
    success_url = reverse_lazy('admin-authors')


class AuthorsUpdate(SuperuserRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'store_admin/author-update.html'
    success_url = reverse_lazy('admin-authors')


# PUBLISHER VIEWS
class PublishersList(SuperuserRequiredMixin, ListView):
    model = Publisher
    template_name = 'store_admin/publishers.html'
    paginate_by = 20


class PublishersCreate(SuperuserRequiredMixin, CreateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'store_admin/publisher-create.html'
    success_url = reverse_lazy('admin-publishers')


class PublishersUpdate(SuperuserRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'store_admin/publisher-update.html'
    success_url = reverse_lazy('admin-publishers')


# ORDER VIEWS
class OrdersList(SuperuserRequiredMixin, ListView):
    model = Order
    template_name = 'store_admin/orders.html'
    paginate_by = 20


class OrdersUpdate(SuperuserRequiredMixin, UpdateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'store_admin/order-update.html'
    success_url = reverse_lazy('admin-orders')

    def post(self, request, *args, **kwargs):
        order = self.get_object()

        books_string = request.POST.get('books')
        books_list = json.loads(books_string)

        for book_quantity in books_list:
            book = Book.objects.get(pk=book_quantity[0])

            try:
                import pdb
                pdb.set_trace()
                order_book = order.orderbooks.get(book=book)
                order_book.quantity = book_quantity[1]
                order_book.save()
            except OrderBook.DoesNotExist:
                OrderBook.objects.create(
                    order=order,
                    book=book,
                    quantity=book_quantity[1],
                    price=book.price
                )

        return redirect('admin-orders')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add users and addresses to the context
        # context['users'] = User.objects.all()
        # Generate addresses JSON
        # addresses_json = {}
        # for user in context['users']:
        #     addresses_json[user.id] = list(
        #         user.addresses.all().values(
        #             'id', 'house', 'street', 'country'
        #         )            # else:
        # context['addresses_json'] = json.dumps(addresses_json)

        context['books'] = Book.objects.all()
        return context
