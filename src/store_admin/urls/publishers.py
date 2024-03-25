from django.urls import path

from .. import views

urlpatterns = [

    # PUBLISHER PATHS
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
    path(
        'publishers/<int:pk>/',
        views.PublisherDetailView.as_view(),
        name='admin-publisher-detail'
    ),
    path(
        'publishers/<int:pk>/delete/',
        views.PublisherDelete.as_view(),
        name='admin-publisher-delete'
    ),
]
