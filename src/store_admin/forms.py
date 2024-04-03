from django.forms import ModelForm

from src.accounts.models import User
from src.books.models import Author, Book, Publisher
from src.shopping.models import Order


class BookCreateForm(ModelForm):

    class Meta:
        model = Book
        fields = [
            'title', 'description', 'price', 'quantity', 'language', 'genre',
            'author', 'publisher'
        ]


class AuthorCreateForm(ModelForm):

    class Meta:
        model = Author
        fields = ['name']


class PublisherCreateForm(ModelForm):

    class Meta:
        model = Publisher
        fields = ['name', 'address']


class OrderCreateForm(ModelForm):

    class Meta:
        model = Order
        fields = ['user', 'address', 'status', 'books']


class UserCreateForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'phone',
            'email',
        ]
