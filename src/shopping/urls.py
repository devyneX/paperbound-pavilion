from django.urls import path

from .views import cart_views

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
    path('checkout', cart_views.checkout, name='checkout'),
]
