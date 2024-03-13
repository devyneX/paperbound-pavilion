from django.forms import ModelForm

from src.books.models import Author, Book, Publisher


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
