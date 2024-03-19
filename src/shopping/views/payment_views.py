from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from src.shopping.models import (
    Order, OrderStatusChoices, PaymentStatusChoices, Transaction
)
from src.shopping.tasks import send_confirmation_email
from src.shopping.utils import (
    init_getway, validate_failure_response, verify_payment
)


class PaymentView(LoginRequiredMixin, View):

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.status != OrderStatusChoices.PENDING:
            return redirect('shopping:cart-detail')
        books = order.books.all()
        amount = order.total_price()
        customer = request.user
        address = order.address
        urls = {
            'success': reverse('shopping:payment_success', kwargs={'pk': pk}),
            'fail': reverse('shopping:payment_fail', kwargs={'pk': pk}),
            'cancel': reverse('shopping:payment_cancel', kwargs={'pk': pk}),
            'ipn': reverse('shopping:ipn', kwargs={'pk': pk})
        }
        tran_id, response = init_getway(
            request, amount, customer, address, books, urls
        )

        if response['status'] == 'SUCCESS':
            Transaction.objects.create(
                order=order,
                transaction_id=tran_id,
                amount=amount,
                currency='BDT',
                status='PENDING'
            )
            return redirect(response['GatewayPageURL'])

        return redirect('shopping:payment_fail', pk=pk)


@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccess(View):

    def post(self, request, pk):
        response = verify_payment(request.POST)
        if response and response['status'] == 'VALID':
            order = get_object_or_404(Order, pk=pk)
            order.status = OrderStatusChoices.PROCESSING
            order.save()
            transaction = Transaction.objects.get(
                transaction_id=response['tran_id']
            )
            transaction.bank_tran_id = response['bank_tran_id']
            transaction.store_amount = response['store_amount']
            transaction.status = PaymentStatusChoices.SUCCESS
            transaction.save()
            messages.success(request, 'Payment Successful')
            send_confirmation_email.delay(order.pk)
        return redirect('shopping:cart-detail')


@method_decorator(csrf_exempt, name='dispatch')
class PaymentFail(View):

    def post(self, request, pk):
        if validate_failure_response(request.POST):
            order = get_object_or_404(Order, pk=pk)
            order.status = OrderStatusChoices.CANCELLED
            order.save()
            cart = {}
            for order_item in order.orderbooks.all():
                order_item.book.quantity += order_item.quantity
                order_item.book.save()

                cart[order_item.book.pk] = order_item.quantity

            request.session['cart'] = cart

            transaction = Transaction.objects.get(
                transaction_id=request.POST['tran_id']
            )
            transaction.status = PaymentStatusChoices.FAILED
            transaction.bank_tran_id = request.POST['bank_tran_id']
            transaction.save()
            messages.error(request, 'Payment Failed')

            return redirect('shopping:cart-detail')


@csrf_exempt
def payment_cancel(request, pk):
    return redirect('shopping:payment_fail', pk=pk)


@csrf_exempt
def ipn(request, pk):
    response = verify_payment(request.POST)
    if response:
        print(response)
    return redirect('shopping:checkout')
