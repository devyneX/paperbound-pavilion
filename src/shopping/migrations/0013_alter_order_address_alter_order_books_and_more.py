# Generated by Django 5.0.3 on 2024-03-22 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_address_city_alter_address_country_and_more'),
        (
            'books',
            '0005_alter_author_created_at_alter_author_deleted_and_more'
        ),
        ('shopping', '0012_transaction_deleted_alter_transaction_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='accounts.address',
                verbose_name='address'
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(
                through='shopping.OrderBook',
                to='books.book',
                verbose_name='books'
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'),
                         ('CONFIRMED', 'Confirmed'), ('SHIPPED', 'Shipped'),
                         ('DELIVERED', 'Delivered'),
                         ('CANCELLED', 'Cancelled')],
                default='PENDING',
                max_length=20,
                verbose_name='status'
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='user'
            ),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='book',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='orderbooks',
                related_query_name='orderbook',
                to='books.book',
                verbose_name='book'
            ),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='order',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='orderbooks',
                related_query_name='orderbook',
                to='shopping.order',
                verbose_name='order'
            ),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='out_of_stock',
            field=models.BooleanField(
                default=False, verbose_name='out_of_stock'
            ),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='price',
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name='price'
            ),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='quantity',
            field=models.IntegerField(verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
    ]
