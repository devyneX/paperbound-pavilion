from django.urls import path

from .. import views

urlpatterns = [

    # ORDER PATHS
    path('orders/', views.OrdersList.as_view(), name='admin-orders'),
    path(
        'orders/update/<int:pk>',
        views.OrdersUpdate.as_view(),
        name='admin-order-update'
    ),
    path(
        'orders/<int:pk>/',
        views.OrderDetailView.as_view(),
        name='admin-order-detail'
    ),
    path(
        'orders/<int:pk>/delete/',
        views.OrderDelete.as_view(),
        name='admin-order-delete'
    ),
]
