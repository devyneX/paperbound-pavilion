import json

from django.db.models import Count, Sum
from django.utils import timezone
from django.views.generic import TemplateView

from src.accounts.models import User
from src.books.models import Author, Book
from src.core.mixins import SuperuserRequiredMixin
from src.shopping.models import Order, Transaction


class AdminBookDashboard(SuperuserRequiredMixin, TemplateView):
    template_name = 'store_admin/analytics/book_analytics.html'

    # template_name = 'store_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate total counts
        total_books = Book.objects.count()
        total_authors = Author.objects.values('name').distinct().count()
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        books_last_30_days = Book.objects.filter(
            created_at__gte=thirty_days_ago
        ).count()
        most_sold_books = Book.objects.annotate(
            total_quantity_sold=Sum('orderbook__quantity')
        ).order_by('-total_quantity_sold')[1:8]
        genre_data = (
            Book.objects.annotate(
                total_quantity_sold=Sum('orderbook__quantity')
            ).exclude(total_quantity_sold=None).values('genre').annotate(
                total_sold=Sum('orderbook__quantity')
            ).order_by('-total_sold')[:7]  # Limiting to top 7 genres
        )
        genre_data = json.dumps(list(genre_data))
        author_data = (
            Book.objects.annotate(
                total_quantity_sold=Sum('orderbook__quantity')
            ).exclude(total_quantity_sold=None).values('author').annotate(
                total_sold=Sum('orderbook__quantity')
            ).order_by('-total_sold')[:7]  # Limiting to top 7 genres
        )
        author_data = json.dumps(list(author_data))
        context.update({
            'total_books': total_books,
            'books_last_30_days': books_last_30_days,
            'total_authors': total_authors,
            'most_sold_books': most_sold_books,
            'genre_data': genre_data,
            'author_data': author_data
        })

        return context


class AdminSaleDashboard(SuperuserRequiredMixin, TemplateView):
    template_name = 'store_admin/analytics/sale_analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_sales = Order.objects.count()
        total_orders = Order.objects.count()
        total_users = User.objects.count()

        # Calculate counts for orders and books in the last 30 days
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        orders_last_30_days = Order.objects.filter(
            created_at__gte=thirty_days_ago
        ).count()
        total_revenue = Transaction.objects.aggregate(
            total_revenue=Sum('amount')
        )['total_revenue']
        sales_by_status = Order.objects.values('status').annotate(
            count=Count('id')
        )
        sales_by_status_data = json.dumps(list(sales_by_status))

        context.update({
            'total_sales': total_sales,
            'total_revenue': total_revenue,
            'total_orders': total_orders,
            'total_users': total_users,
            'orders_last_30_days': orders_last_30_days,
            'sales_by_status_data': sales_by_status_data,
        })
        return context
