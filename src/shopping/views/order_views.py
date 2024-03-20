from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.db.utils import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from src.accounts.models import Address
from src.books.models import Book
from src.shopping.forms import OrderForm
from src.shopping.models import Order, OrderBook


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'shopping/order-history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user
                                    ).order_by('-created_at')


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'shopping/order-detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.orderbooks.annotate(
            title=models.F('book__title')
        ).annotate(
            total_price=models.F('book__price') * models.F('quantity')
        ).values('title', 'quantity', 'price', 'total_price', 'out_of_stock')
        return context


class PlaceOrderView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'shopping/checkout.html'
    form_class = OrderForm

    def get_success_url(self):
        pk = self.object.pk
        return reverse('shopping:payment', kwargs={'pk': pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs

    def form_valid(self, form):
        cart = self.request.session.get('cart', {})
        if len(cart) == 0:
            return redirect('shopping:cart-detail')

        form.instance.user = self.request.user

        self.object = form.save()

        for book_id, quantity in cart.items():
            book = Book.objects.get(id=book_id)
            order_item = OrderBook.objects.create(
                order=self.object,
                book=book,
                price=book.price,
                quantity=quantity
            )
            try:
                book.quantity -= quantity
                book.save()
            except IntegrityError as e:
                print(e)
                order_item.out_of_stock = True
                continue

        self.request.session['cart'] = {}
        return redirect(self.get_success_url())


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['house', 'street', 'city', 'state', 'post_code', 'country']
    template_name = 'shopping/address-create.html'
    success_url = reverse_lazy('shopping:checkout')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
