from django.urls import path

from .. import views

urlpatterns = [
    path('', views.AdminBookDashboard.as_view(), name='admin-book-dashboard'),
    path(
        'book_analytics/',
        views.AdminBookDashboard.as_view(),
        name='admin-book-dashboard'
    ),
    path(
        'sale_analytics/',
        views.AdminSaleDashboard.as_view(),
        name='admin-sale-dashboard'
    ),
]
