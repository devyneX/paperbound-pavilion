from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.UserHomeView.as_view(), name='home'),
]
