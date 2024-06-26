import json

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from src.books.models import Book
from src.shopping.models import Order, OrderBook

from ..forms import OrderCreateForm


# ORDER VIEWS
class OrdersList(PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'store_admin/order/orders.html'
    paginate_by = 20
    permission_required = ('shopping.view_order',)


class OrdersUpdate(PermissionRequiredMixin, UpdateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'store_admin/order/order-update.html'
    success_url = reverse_lazy('admin-orders')
    permission_required = ('shopping.change_order',)

    def post(self, request, *args, **kwargs):
        order = self.get_object()

        books_string = request.POST.get('books')
        books_list = json.loads(books_string)

        for book_quantity in books_list:
            book = Book.objects.get(pk=book_quantity[0])

            try:
                order_book = order.orderbooks.get(book=book)
                order_book.quantity = book_quantity[1]
                order_book.save()
            except OrderBook.DoesNotExist:
                OrderBook.objects.create(
                    order=order,
                    book=book,
                    quantity=book_quantity[1],
                    price=book.price
                )

        return redirect('admin-orders')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add users and addresses to the context
        # context['users'] = User.objects.all()
        # Generate addresses JSON
        # addresses_json = {}
        # for user in context['users']:
        #     addresses_json[user.id] = list(
        #         user.addresses.all().values(
        #             'id', 'house', 'street', 'country'
        #         )            # else:
        # context['addresses_json'] = json.dumps(addresses_json)

        context['books'] = Book.objects.all()
        return context


class OrderDetailView(PermissionRequiredMixin, DetailView):
    model = Order
    template_name = 'store_admin/order/order-detail.html'
    permission_required = ('shopping.view_order',)


class OrderDelete(PermissionRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy(
        'admin-orders'
    )  # Redirect to admin orders list after deletion
    template_name = 'store_admin/order/order-confirm-delete.html'
    permission_required = ('shopping.delete_order',)
