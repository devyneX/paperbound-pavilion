from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from src.books.models import Book
from src.shopping.utils import load_json_request


class AddToCartView(View):

    def post(self, request):
        data = load_json_request(request)
        book_id = data.get('product_id')

        book = Book.objects.get(pk=book_id)

        if book is None:
            return JsonResponse({'error': 'Book not found.'}, status=404)

        if book.quantity < 1:
            return JsonResponse({'error': 'Sorry, this book is out of stock.'},
                                status=200)

        if request.session.get('cart') is None:
            request.session['cart'] = {}

        cart = request.session['cart']

        cart[str(book.pk)] = cart.get(str(book.pk), 0) + 1
        request.session.modified = True

        return JsonResponse({
            'message': 'Book added to cart successfully.',
            'cart_count': cart[str(book.pk)]
        },
                            status=200)


class RemoveFromCartView(View):

    def post(self, request):
        data = load_json_request(request)
        book_id = data.get('product_id')

        book = Book.objects.get(pk=book_id)

        if book is None:
            return JsonResponse({'error': 'Book not found.'}, status=404)

        if request.session.get('cart') is None:
            return JsonResponse({'error': 'Cart is empty.'}, status=400)

        cart = request.session['cart']

        if str(book.pk) not in cart:
            return JsonResponse({'error': 'Book not in cart.'}, status=400)

        cart[str(book.pk)] -= 1
        if cart[str(book.pk)] == 0:
            del cart[str(book.pk)]
        request.session.modified = True

        return JsonResponse({
            'message': 'Book removed from cart successfully.',
            'cart_count': cart[str(book.pk)]
        },
                            status=200)


class DeleteFromCartView(View):

    def post(self, request):
        data = load_json_request(request)
        book_id = data.get('product_id')

        book = Book.objects.get(pk=book_id)

        if book is None:
            return JsonResponse({'error': 'Book not found.'}, status=404)

        if request.session.get('cart') is None:
            return JsonResponse({'error': 'Cart is empty.'}, status=400)

        cart = request.session['cart']

        if str(book.pk) not in cart:
            return JsonResponse({'error': 'Book not in cart.'}, status=400)

        del cart[str(book.pk)]
        request.session.modified = True

        return JsonResponse({
            'message': 'Book removed from cart successfully.',
            'cart_count': 0
        },
                            status=200)


def cart_detail(request):
    cart = request.session.get('cart', {})
    books = Book.objects.filter(id__in=cart.keys())

    book_list = []
    total = 0
    for book in books:
        book_list.append({
            'id': book.pk,
            'title': str(book),
            'price': book.price,
            'quantity': cart[str(book.pk)],
            'total_price': book.price * cart[str(book.pk)],
            'is_in_stock': book.quantity >= cart[str(book.pk)]
        })
        total += book.price * cart[str(book.pk)]

    return render(
        request, 'shopping/cart-detail.html', {
            'books': book_list,
            'total': total
        }
    )
