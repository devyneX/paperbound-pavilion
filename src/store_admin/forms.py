from django.forms import ModelForm

from src.accounts.models import User
from src.books.models import Author, Book, Publisher
from src.shopping.models import Order


class BookCreateForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class AuthorCreateForm(ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class PublisherCreateForm(ModelForm):

    class Meta:
        model = Publisher
        fields = '__all__'


class OrderCreateForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class UserCreateForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'
