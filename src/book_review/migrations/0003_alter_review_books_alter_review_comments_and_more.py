# Generated by Django 5.0.3 on 2024-03-22 08:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0002_review_deleted'),
        (
            'books',
            '0005_alter_author_created_at_alter_author_deleted_and_more'
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='books',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='reviews',
                related_query_name='review',
                to='books.book',
                verbose_name='books'
            ),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments',
            field=models.TextField(verbose_name='comments'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='review',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ratings',
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1)
                ],
                verbose_name='ratings'
            ),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='reviews',
                related_query_name='review',
                to=settings.AUTH_USER_MODEL,
                verbose_name='user'
            ),
        ),
    ]
