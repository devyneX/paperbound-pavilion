from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(
                choices=[('action', 'Action'), ('adventure', 'Adventure'),
                         ('fantasy', 'Fantasy'), ('horror', 'Horror'),
                         ('fiction', 'Fiction'), ('spiritual', 'Spiritual'),
                         ('philosophy', 'Philosophy'), ('mystery', 'Mystery'),
                         ('romance', 'Romance'),
                         ('science_fiction', 'Science Fiction'),
                         ('thriller', 'Thriller'), ('western', 'Western'),
                         ('biography', 'Biography'),
                         ('autobiography', 'Autobiography'),
                         ('comics', 'Comics'), ('cookbook', 'Cookbook'),
                         ('diary', 'Diary'), ('dictionary', 'Dictionary'),
                         ('encyclopedia', 'Encyclopedia'), ('guide', 'Guide'),
                         ('health', 'Health'), ('history', 'History'),
                         ('journal', 'Journal'), ('math', 'Math'),
                         ('memoir', 'Memoir'), ('prayer', 'Prayer'),
                         ('religion', 'Religion'), ('textbook', 'Textbook'),
                         ('poetry', 'Poetry'), ('play', 'Play'),
                         ('satire', 'Satire'), ('science', 'Science'),
                         ('travel', 'Travel'), ('true_crime', 'True Crime')],
                max_length=20
            ),
        ),
    ]
