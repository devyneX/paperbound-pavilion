# Generated by Django 5.0.3 on 2024-03-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_order_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(
                default=None,
                verbose_name=models.CharField(
                    choices=[('PENDING', 'Pending'),
                             ('PROCESSING', 'Processing'),
                             ('SHIPPED', 'Shipped'),
                             ('DELIVERED', 'Delivered'),
                             ('CANCELLED', 'Cancelled')],
                    max_length=20
                )
            ),
            preserve_default=False,
        ),
    ]
