import json
from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from src.accounts.models import User
from src.books.models import Book
from src.shopping.models import Order, Transaction


def dashboard_callback(request, context):
    name = 'Admin'

    if request.user.last_name:
        name = request.user.last_name
    elif request.user.first_name:
        name = request.user.first_name

    thirty_days_ago = timezone.now() - timedelta(days=30)
    total_sales = Transaction.objects.filter(status='SUCCESS',).aggregate(
        total=models.Sum('amount')
    )['total']

    total_user = User.objects.count()
    total_books = Book.objects.count()
    total_orders = Order.objects.count()

    sales_queryset = Order.objects.filter(
        status='CONFIRMED',
        created_at__date__range=[thirty_days_ago,
                                 timezone.now()]
    ).annotate(
        total_price=models.F('orderbook__quantity') *
        models.F('orderbook__price')
    ).values('created_at__date').annotate(total=models.Sum('total_price'))

    sales_labels = [
        x.get('created_at__date').strftime('%d-%m-%y') for x in sales_queryset
    ]
    print(sales_labels)
    sales_data = [float(x.get('total')) for x in sales_queryset]

    # best_selling_books = Book.objects.annotate(
    #     total_quantity_sold=models.Sum('orderbook__quantity')
    # ).order_by('-total_quantity_sold')[:3]

    context.update(
        {
            'navigation': [
                {'title': _('Dashboard'), 'link': '/', 'active': True},
                {'title': _('Analytics'), 'link': '#'},
                {'title': _('Settings'), 'link': '#'},
            ],
            'filters': [
                {'title': _('All'), 'link': '#', 'active': True},
                {
                    'title': _('New'),
                    'link': '#',
                },
            ],
            'welcome': {
                'title': f'Welcome, {name}',
            },
            'sales': {
                'total_sales': total_sales,
            },
            'kpi': [
                {
                    'title': 'Total Users',
                    'metric': total_user,
                },
                {
                    'title': 'Total Books',
                    'metric': total_books,
                },
                {
                    'title': 'Total Orders',
                    'metric': total_orders,
                },
            ],
            'chart': json.dumps(
                {
                    'labels': sales_labels,
                    'datasets': [
                        {
                            'label': 'Example 1',
                            # 'type': 'line',
                            'data': sales_data,
                            'backgroundColor': '#f0abfc',
                            'borderColor': '#f0abfc',
                        },
                    ],
                }
            ),
        },
    )

    return context
