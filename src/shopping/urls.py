from django.urls import path

from .views import cart_views, order_views, payment_views

app_name = 'shopping'

urlpatterns = [
    path('cart/add/', cart_views.AddToCartView.as_view(), name='add_to_cart'),
    path(
        'cart/remove/',
        cart_views.RemoveFromCartView.as_view(),
        name='remove_from_cart'
    ),
    path(
        'cart/delete/',
        cart_views.DeleteFromCartView.as_view(),
        name='delete_from_cart'
    ),
    path('cart/', cart_views.cart_detail, name='cart-detail'),
    path(
        'orders/',
        order_views.OrderHistoryView.as_view(),
        name='order-history'
    ),
    path(
        'order/<int:pk>/',
        order_views.OrderDetailView.as_view(),
        name='order-detail'
    ),
    path('checkout/', order_views.PlaceOrderView.as_view(), name='checkout'),
    path(
        'payment/<int:pk>/',
        payment_views.PaymentView.as_view(),
        name='payment'
    ),
    path(
        'payment/<int:pk>/success/',
        payment_views.PaymentSuccess.as_view(),
        name='payment_success'
    ),
    path(
        'payment/<int:pk>/fail/',
        payment_views.PaymentFail.as_view(),
        name='payment_fail'
    ),
    path(
        'payment/<int:pk>/cancel/',
        payment_views.payment_cancel,
        name='payment_cancel'
    ),
    path('payment/<int:pk>/ipn/', payment_views.ipn, name='ipn'),
]
