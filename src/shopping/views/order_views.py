from django.contrib import messages
from django.db.utils import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView

from src.accounts.models import Address
from src.books.models import Book

from ..forms import OrderForm
from ..models import Order, OrderBook, Transaction
from ..utils import init_getway, verify_payment


class PlaceOrderView(CreateView):
    model = Order
    template_name = 'shopping/checkout.html'
    form_class = OrderForm

    def get_success_url(self):
        pk = self.object.pk
        return reverse('shopping:payment', kwargs={'id': pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs

    def form_valid(self, form):
        cart = self.request.session.get('cart', {})
        if len(cart) == 0:
            return redirect('shopping:cart_detail')

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
        return self.get_success_url()


class AddressCreateView(CreateView):
    model = Address
    fields = ['house', 'street', 'city', 'state', 'post_code', 'country']
    template_name = 'shopping/address-create.html'
    success_url = reverse_lazy('shopping:checkout')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PaymentView(View):

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        books = order.books.all()
        amount = order.total_price()
        customer = request.user
        address = Address.objects.get(user=customer)
        urls = {
            'success': reverse('shopping:post_payment', kwargs={'id': id}),
            'fail': reverse('shopping:post_payment', kwargs={'id': id}),
            'cancel': reverse('shopping:post_payment', kwargs={'id': id}),
            'ipn': reverse('shopping:ipn', kwargs={'id': id})
        }
        response = init_getway(request, amount, customer, address, books, urls)

        if response['status'] == 'SUCCESS':
            Transaction.objects.create(
                order=order,
                id=response['tran_id'],
                amount=amount,
                currency='BDT',
                status='PENDING'
            )
            return redirect(response['GatewayPageURL'])

        return redirect('shopping:payment_fail', pk=pk)


@csrf_exempt
def post_payment(request, pk):
    messages.info(
        request, 'You will receive a confirmation email shortly after payment \
            validation.'
    )
    # change this to dashboard
    return redirect('shopping:checkout')


# @csrf_exempt
# def payment_success(request, id):
#     print(f'successful payment for order-{id}')
#     print(request.POST)
#     return redirect('shopping:checkout')

# @csrf_exempt
# def payment_fail(request, id):
#     print('fail:', request.POST)
#     return redirect('shopping:checkout')

# @csrf_exempt
# def payment_cancel(request, id):
#     return redirect('shopping:payment_fail', id=id)


@csrf_exempt
def ipn(request, pk):
    response = verify_payment(request.POST)
    if response:
        print(response)
    return redirect('shopping:checkout')
