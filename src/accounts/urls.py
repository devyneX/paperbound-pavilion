from django.urls import path

from src.accounts.views import auth_views, profile_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.Login.as_view(), name='login'),
    path('register/', auth_views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.Logout.as_view(), name='logout'),
    path(
        'profile/',
        profile_views.SelfProfileView.as_view(),
        name='self-profile'
    ),
    path(
        'profile/update/',
        profile_views.ProfileUpdateView.as_view(),
        name='profile-update'
    ),
    path(
        'profile/<str:username>',
        profile_views.ProfileView.as_view(),
        name='profile'
    ),
    path(
        'address/add/',
        profile_views.AddressCreateView.as_view(),
        name='address-create'
    ),
    path(
        'addresses/',
        profile_views.AddressListView.as_view(),
        name='address-list'
    ),
    path(
        'address/<int:pk>/update/',
        profile_views.AddressUpdateView.as_view(),
        name='address-update'
    ),
]
