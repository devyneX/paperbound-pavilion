from django.urls import path

from .. import views

urlpatterns = [
    # BOOK PATHS
    path('books/', views.BooksList.as_view(), name='admin-books'),
    path(
        'books/create/', views.BooksCreate.as_view(), name='admin-book-create'
    ),
    path(
        'books/update/<int:pk>',
        views.BooksUpdate.as_view(),
        name='admin-book-update'
    ),
    path(
        'books/<int:pk>/',
        views.BookDetailView.as_view(),
        name='admin-book-detail'
    ),
    path(
        'books/<int:pk>/delete/',
        views.BookDelete.as_view(),
        name='admin-book-delete'
    ),
]
