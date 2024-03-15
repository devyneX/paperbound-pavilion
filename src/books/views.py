from django.apps import apps
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Book

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
    paginate_by = 30
    context_object_name = 'book_list'
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_details.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        reviews = Review.objects.filter(books__id=pk)
        context = {'book': book, 'reviews': reviews[:3]}
        return render(request, self.template_name, context)
