# Generated by Django 5.0.3 on 2024-03-22 08:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_merge_20240319_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='author',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='books',
                related_query_name='book',
                to='books.author',
                verbose_name='author'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
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
                max_length=20,
                verbose_name='genre'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(
                choices=[
                    ('aa', 'Afar'), ('ab', 'Abkhazian'), ('af', 'Afrikaans'),
                    ('ak', 'Akan'), ('sq', 'Albanian'), ('am', 'Amharic'),
                    ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'),
                    ('as', 'Assamese'), ('av', 'Avaric'), ('ae', 'Avestan'),
                    ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'),
                    ('bm', 'Bambara'), ('eu', 'Basque'), ('be', 'Belarusian'),
                    ('bn', 'Bengali'), ('bh', 'Bihari languages'),
                    ('bi', 'Bislama'), ('bo', 'Tibetan'), ('bs', 'Bosnian'),
                    ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'),
                    ('ca', 'Catalan; Valencian'), ('cs', 'Czech'),
                    ('ch', 'Chamorro'), ('ce', 'Chechen'), ('zh', 'Chinese'),
                    (
                        'cu',
                        'Church Slavic; Old Slavonic; Church Slavonic;         Old Bulgarian; Old Church Slavonic'
                    ), ('cv', 'Chuvash'), ('kw', 'Cornish'),
                    ('co', 'Corsican'), ('cr', 'Cree'), ('cy', 'Welsh'),
                    ('da', 'Danish'), ('de', 'German'),
                    ('dv', 'Divehi; Dhivehi; Maldivian'),
                    ('nl', 'Dutch; Flemish'), ('dz', 'Dzongkha'),
                    ('el', 'Greek, Modern (1453-)'), ('en', 'English'),
                    ('eo', 'Esperanto'), ('et', 'Estonian'), ('ee', 'Ewe'),
                    ('fo', 'Faroese'), ('fa', 'Persian'), ('fj', 'Fijian'),
                    ('fi', 'Finnish'), ('fr', 'French'),
                    ('fy', 'Western Frisian'), ('ff', 'Fulah'),
                    ('gd', 'Gaelic; Scottish Gaelic'), ('ga', 'Irish'),
                    ('gl', 'Galician'), ('gv', 'Manx'), ('gn', 'Guarani'),
                    ('gu', 'Gujarati'), ('ht', 'Haitian; Haitian Creole'),
                    ('ha', 'Hausa'), ('he', 'Hebrew'), ('hz', 'Herero'),
                    ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hr', 'Croatian'),
                    ('hu', 'Hungarian'), ('ig', 'Igbo'), ('is', 'Icelandic'),
                    ('io', 'Ido'), ('ii', 'Sichuan Yi; Nuosu'),
                    ('iu', 'Inuktitut'), ('ie', 'Interlingue; Occidental'),
                    (
                        'ia',
                        'Interlingua (International Auxiliary Language Association)'
                    ), ('id', 'Indonesian'), ('ik', 'Inupiaq'),
                    ('it', 'Italian'), ('jv', 'Javanese'), ('ja', 'Japanese'),
                    ('kl', 'Kalaallisut; Greenlandic'), ('kn', 'Kannada'),
                    ('ks', 'Kashmiri'), ('ka', 'Georgian'), ('kk', 'Kazakh'),
                    ('km', 'Central Khmer'), ('ki', 'Kikuyu; Gikuyu'),
                    ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz; Kyrgyz'),
                    ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'),
                    ('kj', 'Kuanyama; Kwanyama'), ('ku', 'Kurdish'),
                    ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'),
                    ('li', 'Limburgan; Limburger; Limburgish'),
                    ('ln', 'Lingala'), ('lt', 'Lithuanian'),
                    ('lb', 'Luxembourgish; Letzeburgesch'),
                    ('lu', 'Luba-Katanga'), ('lg', 'Ganda'),
                    ('mk', 'Macedonian'), ('mh', 'Marshallese'),
                    ('ml', 'Malayalam'), ('mi', 'Maori'), ('mr', 'Marathi'),
                    ('ms', 'Malay'), ('mt', 'Maltese'), ('mn', 'Mongolian'),
                    ('na', 'Nauru'), ('nv', 'Navajo; Navaho'),
                    ('nr', 'Ndebele, South; South Ndebele'),
                    ('nd', 'Ndebele, North; North Ndebele'), ('ne', 'Nepali'),
                    ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
                    ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
                    ('no', 'Norwegian'), ('oc', 'Occitan (post 1500)'),
                    ('oj', 'Ojibwa'), ('or', 'Oriya'), ('om', 'Oromo'),
                    ('os', 'Ossetian')
                ],
                max_length=3,
                verbose_name='language'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name='price'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='books',
                related_query_name='book',
                to='books.publisher',
                verbose_name='publisher'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name='quantity'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.TextField(verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='created_at'
            ),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='deleted_at'
            ),
        ),
    ]