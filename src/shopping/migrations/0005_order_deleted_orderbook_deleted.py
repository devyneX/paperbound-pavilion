# Generated by Django 5.0.3 on 2024-03-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderbook',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
