from django.urls import path

from .views import BookDetailView, BookListView, BookSearch

booksurlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('search/', BookSearch.as_view(), name='book-search'),
]
