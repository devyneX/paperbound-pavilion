from django.urls import path

from . import views

urlpatterns = [
    # path('login/', views.AdminLogin.as_view(), name='admin-login'),
    path('dashboard/', views.AdminDashboard.as_view(), name='admin-dashboard'),

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

    # PUBLISHER PATHS
    path('authors/', views.AuthorList.as_view(), name='admin-authors'),
    path(
        'authors/create/',
        views.AuthorCreate.as_view(),
        name='admin-author-create'
    ),
    path(
        'authors/update/<int:pk>',
        views.AuthorsUpdate.as_view(),
        name='admin-author-update'
    ),

    # AUTHOR PATHS
    # path('books/', views.BooksList.as_view(), name='admin-books'),
    # path(
    #     'books/create/', views.BooksCreate.as_view(), name='admin-book-create' # noqa
    # ),
    # path(
    #     'books/update/<int:pk>',
    #     views.BooksUpdate.as_view(),
    #     name='admin-book-update'
    # ),
]
