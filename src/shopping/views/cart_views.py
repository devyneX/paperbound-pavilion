from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from src.books.models import Book


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.quantity < 1:
        messages.error(request, 'Sorry, this book is out of stock.')
        # TODO: redirect to book list page
        return redirect('shopping:cart-detail')

    if request.session.get('cart') is None:
        request.session['cart'] = {}

    cart = request.session['cart']

    cart[str(book.pk)] = cart.get(str(book.pk), 0) + 1
    request.session.modified = True
    messages.success(request, 'Book added to cart successfully.')
    return redirect('shopping:cart-detail')


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


def remove_from_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.session.get('cart') is None:
        return redirect('shopping:cart-detail')

    cart = request.session['cart']

    if str(book.pk) in cart:
        cart[str(book.pk)] -= 1
        if cart[str(book.pk)] == 0:
            del cart[str(book.pk)]
        request.session.modified = True
        messages.success(request, 'Book removed from cart successfully.')
    return redirect('shopping:cart-detail')


def delete_cart_item(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.session.get('cart') is None:
        return redirect('shopping:cart-detail')

    cart = request.session['cart']

    if str(book.pk) in cart:
        del cart[str(book.pk)]
        request.session.modified = True
        messages.success(request, 'Book removed from cart successfully.')
    return redirect('shopping:cart-detail')
