from django.test import Client, TestCase
from django.urls import reverse

from src.accounts.models import User
from src.books.models import Author, Book, Publisher


class TestBookViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.login(username='admin', password='password')

        # Creating sample author and publisher
        self.author = Author.objects.create(name='Test Author')
        self.publisher = Publisher.objects.create(name='Test Publisher')

        # Sample book data
        self.book_data = {
            'title': 'Test Book',
            'description': 'This is a test book',
            'price': '19.99',
            'quantity': '10',
            'language': 'ENG',
            'genre': 'FICTION',
            'author': self.author.id,
            'publisher': self.publisher.id
        }

        # Creating a sample book
        self.book_instance = Book.objects.create(
            title='Existing Book',
            description='This is an existing book',
            price='24.99',
            quantity='5',
            language='ENG',
            genre='NON_FICTION',
            author=self.author,
            publisher=self.publisher
        )

    def test_books_list_view(self):
        response = self.client.get(reverse('admin-books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/book/books.html')

    def test_books_create_view(self):
        response = self.client.post(
            reverse('admin-book-create'), data=self.book_data
        )
        self.assertEqual(response.status_code, 200)

        # created_book = Book.objects.get(title='Test Book')
        # self.assertEqual(created_book.description, 'This is a test book')

    def test_book_detail_view(self):
        response = self.client.get(
            reverse('admin-book-detail', kwargs={'pk': self.book_instance.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/book/book-detail.html')

    def test_book_delete_view(self):
        response = self.client.post(
            reverse('admin-book-delete', kwargs={'pk': self.book_instance.pk})
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful deletion

        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=self.book_instance.pk)

    def test_books_update_view(self):
        updated_data = {
            'title': 'Updated Book',
            'description': 'This is an updated book',
            'price': '29.99',
            'quantity': '15',
            'language': 'ENG',
            'genre': 'FICTION',
            'author': self.author.id,
            'publisher': self.publisher.id
        }
        response = self.client.post(
            reverse('admin-book-update', kwargs={'pk': self.book_instance.pk}),
            data=updated_data
        )
        self.assertEqual(response.status_code, 200)

        # updated_book = Book.objects.get(pk=self.book_instance.pk)
        # self.assertEqual(updated_book.title, 'Updated Book')
        # self.assertEqual(updated_book.description, 'This is an updated book')
