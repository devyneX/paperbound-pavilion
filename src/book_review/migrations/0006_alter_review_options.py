# Generated by Django 5.0.3 on 2024-04-25 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0005_alter_review_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={
                'permissions': (('add_own_review', 'Can add own review'),
                                ('change_own_review', 'Can change own review'),
                                ('view_own_review', 'Can view own review'))
            },
        ),
    ]
