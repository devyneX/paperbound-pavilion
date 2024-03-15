from django.urls import path

from .views import cart_views, order_views

app_name = 'shopping'

urlpatterns = [
    path(
        'cart/add/<int:book_id>/', cart_views.add_to_cart, name='add_to_cart'
    ),
    path(
        'cart/remove/<int:book_id>/',
        cart_views.remove_from_cart,
        name='remove_from_cart'
    ),
    path('cart', cart_views.cart_detail, name='cart-detail'),
    path('checkout', order_views.PlaceOrderView.as_view(), name='checkout'),
    path(
        'address/add',
        order_views.AddressCreateView.as_view(),
        name='address-create'
    ),
    path(
        'payment/<int:pk>', order_views.PaymentView.as_view(), name='payment'
    ),
    path('payment/<int:pk>/ipn', order_views.ipn, name='ipn'),
    path('payment/forward', order_views.post_payment, name='post-payment'),
]
