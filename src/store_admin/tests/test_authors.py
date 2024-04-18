from django.test import Client, TestCase
from django.urls import reverse

from src.accounts.models import User
from src.books.models import Author


class TestAuthorViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.login(username='admin', password='password')

        # Creating sample author
        self.author_data = {'name': 'Test Author'}

        # Creating a sample author instance
        self.author_instance = Author.objects.create(name='Existing Author')

    def test_authors_list_view(self):
        response = self.client.get(reverse('admin-authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/author/authors.html')

    def test_authors_create_view(self):
        response = self.client.post(
            reverse('admin-author-create'), data=self.author_data
        )
        self.assertEqual(response.status_code, 302)

        # created_author = Author.objects.get(name='Test Author')
        # self.assertEqual(created_author.name, 'Test Author')

    def test_author_detail_view(self):
        response = self.client.get(
            reverse(
                'admin-author-detail', kwargs={'pk': self.author_instance.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'store_admin/author/author-detail.html'
        )

    def test_author_delete_view(self):
        response = self.client.post(
            reverse(
                'admin-author-delete', kwargs={'pk': self.author_instance.pk}
            )
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful deletion

        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(pk=self.author_instance.pk)

    def test_authors_update_view(self):
        updated_data = {'name': 'Updated Author'}
        response = self.client.post(
            reverse(
                'admin-author-update', kwargs={'pk': self.author_instance.pk}
            ),
            data=updated_data
        )
        self.assertEqual(response.status_code, 302)

        # updated_author = Author.objects.get(pk=self.author_instance.pk)
        # self.assertEqual(updated_author.name, 'Updated Author')
