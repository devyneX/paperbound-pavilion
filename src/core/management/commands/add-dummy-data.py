from django.core.management.base import BaseCommand, CommandError

from src.core.management.commands._private import (
    add_dummy_authors, add_dummy_books, add_dummy_orders, add_dummy_publishers,
    add_dummy_users, delete_all_data
)


class Command(BaseCommand):
    help = 'Add dummy data to the database'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete', action='store_true', help='Delete all existing data'
        )
        parser.add_argument(
            '--exclude-users',
            action='store_true',
            help='Exclude adding dummy users'
        )
        parser.add_argument(
            '--exclude-authors',
            action='store_true',
            help='Exclude adding dummy authors'
        )
        parser.add_argument(
            '--exclude-publishers',
            action='store_true',
            help='Exclude adding dummy publishers'
        )
        parser.add_argument(
            '--exclude-books',
            action='store_true',
            help='Exclude adding dummy books'
        )
        parser.add_argument(
            '--exclude-orders',
            action='store_true',
            help='Exclude adding dummy orders'
        )

    def handle(self, *args, **options):
        delete = options.get('delete', False)
        exclude_users = options.get('exclude_users', False)
        exclude_authors = options.get('exclude_authors', False)
        exclude_publishers = options.get('exclude_publishers', False)
        exclude_books = options.get('exclude_books', False)
        exclude_orders = options.get('exclude_orders', False)

        if delete:
            self.stdout.write('Deleting all existing data...')
            delete_all_data()
            self.stdout.write(
                self.style.SUCCESS('All existing data deleted successfully.')
            )

        if (
            exclude_users and exclude_authors and exclude_publishers and
            exclude_books and exclude_orders and not delete
        ):
            raise CommandError(
                'All data types are excluded. No data will be added.'
            )

        if not exclude_users:
            self.stdout.write('Adding dummy users and addresses...')
            add_dummy_users()
            self.stdout.write(
                self.style.SUCCESS('Dummy users added successfully.')
            )

        if not exclude_authors:
            self.stdout.write('Adding dummy authors...')
            add_dummy_authors()
            self.stdout.write(
                self.style.SUCCESS('Dummy authors added successfully.')
            )

        if not exclude_publishers:
            self.stdout.write('Adding dummy publishers...')
            add_dummy_publishers()
            self.stdout.write(
                self.style.SUCCESS('Dummy publishers added successfully.')
            )

        if not exclude_books:
            self.stdout.write('Adding dummy books and reviews...')
            add_dummy_books()
            self.stdout.write(
                self.style.SUCCESS('Dummy books added successfully.')
            )

        if not exclude_orders:
            self.stdout.write('Adding dummy orders and transactions...')
            add_dummy_orders()
            self.stdout.write(
                self.style.SUCCESS('Dummy orders added successfully.')
            )

        self.stdout.write(self.style.SUCCESS('Dummy data added successfully.'))
