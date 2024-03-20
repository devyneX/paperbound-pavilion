from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserHomeView.as_view(), name='home'),
    path('set-language/', views.set_language, name='set_language'),
]
