from django.shortcuts import get_object_or_404, render  # noqa
from django.views.generic import DetailView, ListView

from .models import Book


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
        context = {'book': book}
        return render(request, self.template_name, context)
