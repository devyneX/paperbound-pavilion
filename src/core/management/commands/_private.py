import random
import uuid

from django.db import IntegrityError
from faker import Faker

from src.accounts.models import Address, User
from src.book_review.models import Review
from src.books.models import Author, Book, Publisher
from src.shopping.models import (
    Order, OrderStatusChoices, PaymentStatusChoices, Transaction
)

fake = Faker()


def delete_all_data():
    Transaction.objects.all().delete()
    Order.objects.all().delete()
    Review.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    Publisher.objects.all().delete()
    Address.objects.all().delete()
    User.objects.exclude(is_superuser=True).delete()


def add_dummy_users():
    for i in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = first_name.lower() + last_name.lower()
        email = username + '@dummy.com'
        phone = fake.random_number(digits=20)
        try:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                phone=phone,
                password='password',
            )
        except IntegrityError:
            username = username + str(i)
            email = username + '@dummy.com'
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                phone=phone,
                email=email,
                password='password',
            )

        add_dummy_addresses(user)


def add_dummy_addresses(user):
    address_count = random.randint(1, 5)

    for _ in range(address_count):
        Address.objects.create(
            user=user,
            house=fake.building_number(),
            street=fake.street_name(),
            city=fake.city(),
            state=fake.state(),
            country=random.choice([
                choice[0] for choice in Address.country.field.choices
            ]),
            post_code=fake.postcode(),
        )


def add_dummy_orders():
    queryset = User.objects.exclude(is_superuser=True)
    for _ in range(100):
        user = queryset.order_by('?').first()
        address = user.addresses.order_by('?').first()
        order = Order.objects.create(
            user=user,
            address=address,
            status=random.choice([
                OrderStatusChoices.CONFIRMED, OrderStatusChoices.SHIPPED,
                OrderStatusChoices.DELIVERED, OrderStatusChoices.CANCELLED
            ])
        )
        add_dummy_order_books(order)
        add_dummy_transaction(order)


def add_dummy_order_books(order):
    book_count = random.randint(1, 10)
    books = Book.objects.order_by('?')[:book_count]

    for book in books:
        order.orderbooks.create(
            order=order,
            book=book,
            quantity=random.randint(1, 10),
            price=book.price,
        )


def add_dummy_transaction(order):
    if order.status != OrderStatusChoices.CANCELLED:
        Transaction.objects.create(
            transaction_id=uuid.uuid4(),
            order=order,
            status=PaymentStatusChoices.SUCCESS,
            amount=order.total_price(),
        )
    else:
        Transaction.objects.create(
            order=order,
            transaction_id=uuid.uuid4(),
            status=PaymentStatusChoices.FAILED,
            amount=order.total_price(),
            currency='BDT'
        )


def add_dummy_authors():
    for _ in range(30):
        Author.objects.create(name=fake.name())


def add_dummy_publishers():
    for _ in range(30):
        Publisher.objects.create(name=fake.company(), address=fake.address())


def add_dummy_books():
    author_queryset = Author.objects.all()
    publisher_queryset = Publisher.objects.all()
    for _ in range(100):
        author = author_queryset.order_by('?').first()
        publisher = publisher_queryset.order_by('?').first()
        book = Book.objects.create(
            title=fake.catch_phrase(),
            description=fake.paragraph(),
            price=random.uniform(5, 100),
            quantity=random.randint(1, 100),
            language=random.choice([
                choice[0] for choice in Book.language.field.choices
            ]),
            genre=random.choice([
                choice[0] for choice in Book.genre.field.choices
            ]),
            author=author,
            publisher=publisher,
        )

        add_dummy_reviews(book)


def add_dummy_reviews(book):
    review_count = random.randint(1, 100)
    for _ in range(review_count):
        user = User.objects.order_by('?').first()
        book.reviews.create(
            user=user,
            ratings=random.randint(1, 5),
            comments=fake.paragraph(),
        )
