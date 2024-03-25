from django.urls import path

from .. import views

urlpatterns = [

    # USER PATHS
    path('users/', views.UsersList.as_view(), name='admin-users'),
    path(
        'users/create/', views.UsersCreate.as_view(), name='admin-user-create'
    ),
    path(
        'users/update/<int:pk>',
        views.UsersUpdate.as_view(),
        name='admin-user-update'
    ),
    path(
        'users/<int:pk>/',
        views.UserDetailView.as_view(),
        name='admin-user-detail'
    ),
    path(
        'users/<int:pk>/delete/',
        views.UserDelete.as_view(),
        name='admin-user-delete'
    ),
]
