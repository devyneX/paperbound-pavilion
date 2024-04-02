from django.contrib.postgres.search import SearchVector
from django.db.models import Q

from .models import Book


def books_search(request):
    books = Book.objects.all()

    # Search by author name using full-text search
    author_query = request.GET.get('author')
    if author_query:
        books = books.annotate(author_search=SearchVector('author__name'),
                               ).filter(author_search=author_query)

    # Search by book name using full-text search
    book_name_query = request.GET.get('book_name')
    if book_name_query:
        books = books.annotate(book_name_search=SearchVector('title'),).filter(
            book_name_search=book_name_query
        )

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

    return books


def books_general_search(request):
    books = Book.objects.all()

    # Search by author name using full-text search
    query = request.GET.get('query')

    if not query:
        return None

    books = books.annotate(
        author_search=SearchVector('author__name'),
        book_name_search=SearchVector('title'),
    ).filter(
        Q(author_search=query) | Q(book_name_search=query) |
        Q(genre__icontains=query)
    )

    return books
