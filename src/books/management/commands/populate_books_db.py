# app_name/management/commands/populate_db.py

import random

from django.core.management.base import BaseCommand
from faker import Faker

from src.books.models import Author, Book, Publisher

fake = Faker()


class Command(BaseCommand):
    # help = 'Populate the database with random data'

    def add_arguments(self, parser):
        parser.add_argument(
            'total',
            type=int,
            help='Indicates the number of records to be created'
        )

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for _ in range(total):
            # Create an author
            author = Author.objects.create(name=fake.name())

            # Create a publisher
            publisher = Publisher.objects.create(
                name=fake.company(), address=fake.address()
            )

            # Create a book
            Book.objects.create(
                title=fake.catch_phrase(),
                description=fake.paragraph(),
                price=random.uniform(5, 100),
                quantity=random.randint(1, 100),
                language=random.choice(
                    ['EN', 'FR', 'ES']
                ),  # Assuming LanguageChoices is defined accordingly
                genre=random.choice([
                    'fiction', 'spiritual', 'sci-fi', 'horror'
                ]),  # Assuming GenreChoices is defined accordingly
                author=author,
                publisher=publisher
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated the database with {total} records'
            )
        )
