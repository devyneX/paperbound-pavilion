from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from src.accounts.models import User
from src.books.models import Book


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class BookCreateForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
