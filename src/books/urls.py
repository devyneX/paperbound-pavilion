from django.urls import path

from .views import BookDetailView, BookListView

booksurlpatterns = [
    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book'),
]
