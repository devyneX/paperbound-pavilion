from django.urls import path

from . import views

urlpatterns = [
    # path('login/', views.AdminLogin.as_view(), name='admin-login'),
    path('', views.AdminDashboard.as_view(), name='admin-dashboard'),

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
    path('authors/', views.AuthorsList.as_view(), name='admin-authors'),
    path(
        'authors/create/',
        views.AuthorsCreate.as_view(),
        name='admin-author-create'
    ),
    path(
        'authors/update/<int:pk>',
        views.AuthorsUpdate.as_view(),
        name='admin-author-update'
    ),

    # AUTHOR PATHS
    path(
        'publishers/', views.PublishersList.as_view(), name='admin-publishers'
    ),
    path(
        'publishers/create/',
        views.PublishersCreate.as_view(),
        name='admin-publisher-create'
    ),
    path(
        'publishers/update/<int:pk>',
        views.PublishersUpdate.as_view(),
        name='admin-publisher-update'
    ),

    # ORDER PATHS
    path('orders/', views.OrdersList.as_view(), name='admin-orders'),
    path(
        'orders/update/<int:pk>',
        views.OrdersUpdate.as_view(),
        name='admin-order-update'
    ),
]
