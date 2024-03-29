# Generated by Django 5.0.3 on 2024-03-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(
                choices=[('PENDING', 'Pending'), ('SUCCESS', 'Success'),
                         ('FAILED', 'Failed'), ('CANCELLED', 'Cancelled')],
                default='PENDING',
                max_length=10
            ),
        ),
    ]
