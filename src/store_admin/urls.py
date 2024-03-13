from django.urls import path

from . import views

urlpatterns = [
    # path('login/', views.AdminLogin.as_view(), name='admin-login'),
    path('dashboard/', views.AdminDashboard.as_view(), name='admin-dashboard'),
    path('books/', views.BooksList.as_view(), name='admin-books'),
]
