from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, ListView

from .choices import GenreChoices, LanguageChoices
from .models import Author, Book, Publisher

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
        review = Review.objects.filter(pk=pk)
        context = {'book': book, 'review': review[:3]}
        return render(request, self.template_name, context)


class BookSearch(View):

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()

        # Search by author name using full-text search
        author_query = request.GET.get('author')
        if author_query:
            books = books.annotate(
                author_search=SearchVector('author__name'),
            ).filter(author_search=author_query)

        # Search by book name using full-text search
        book_name_query = request.GET.get('book_name')
        if book_name_query:
            books = books.annotate(book_name_search=SearchVector('name'),
                                   ).filter(book_name_search=book_name_query)

        # Search by publisher name using full-text search
        publisher_query = request.GET.get('publisher')
        if publisher_query:
            books = books.annotate(
                publisher_search=SearchVector('publisher__name'),
            ).filter(publisher_search=publisher_query)

        # Filter by price range
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if min_price and max_price:
            books = books.filter(price__range=(min_price, max_price))

        # Filter by publication date range
        # start_date = request.GET.get('start_date')
        # end_date = request.GET.get('end_date')
        # if start_date and end_date:
        #     books = books.filter(
        #         publication_date__range=(start_date, end_date)
        #     )

        # Filter by book genre
        genre = request.GET.get('genre')
        if genre:
            books = books.filter(genre=genre)

        # Filter by book language
        language = request.GET.get('language')
        if language:
            books = books.filter(language=language)

        # Filter by publisher name
        publisher = request.GET.get('publisher')
        if publisher:
            books = books.filter(publisher__name=publisher)

        context = {}
        context['books'] = books
        context['genres'] = GenreChoices.choices
        context['languages'] = LanguageChoices.choices
        # Add authors to the context
        context['authors'] = Author.objects.all()
        # Add publishers to the context
        context['publishers'] = Publisher.objects.all()
        context['params'] = request.GET

        return render(request, 'book_search_result.html', context)
