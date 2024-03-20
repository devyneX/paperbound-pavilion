from django.urls import path

from .views import cart_views, order_views, payment_views

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
    path('cart/', cart_views.cart_detail, name='cart-detail'),
    path(
        'cart/delete/<int:book_id>/',
        cart_views.delete_cart_item,
        name='delete_from_cart'
    ),
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
        'address/add/',
        order_views.AddressCreateView.as_view(),
        name='address-create'
    ),
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
