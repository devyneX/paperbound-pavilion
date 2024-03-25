from django.urls import path

from .. import views

urlpatterns = [
    # AUTHOR PATHS
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
    path(
        'authors/<int:pk>/',
        views.AuthorDetailView.as_view(),
        name='admin-author-detail'
    ),
    path(
        'authors/<int:pk>/delete/',
        views.AuthorDelete.as_view(),
        name='admin-author-delete'
    ),
]
