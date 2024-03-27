from django.utils import timezone
from django.views.generic import TemplateView

from src.accounts.models import User
from src.books.models import Book
from src.core.mixins import SuperuserRequiredMixin
from src.shopping.models import Order


class AdminDashboard(SuperuserRequiredMixin, TemplateView):
    template_name = 'store_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate total counts
        total_books = Book.objects.count()
        total_orders = Order.objects.count()
        total_users = User.objects.count()

        # Calculate counts for orders and books in the last 30 days
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
        orders_last_30_days = Order.objects.filter(
            created_at__gte=thirty_days_ago
        ).count()
        books_last_30_days = Book.objects.filter(
            created_at__gte=thirty_days_ago
        ).count()

        context.update({
            'total_books': total_books,
            'total_orders': total_orders,
            'total_users': total_users,
            'orders_last_30_days': orders_last_30_days,
            'books_last_30_days': books_last_30_days,
        })

        return context
