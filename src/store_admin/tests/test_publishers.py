from django.test import TestCase, Client
from django.urls import reverse
from src.accounts.models import User
from src.books.models import Publisher

class TestPublisherViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')
        self.client.login(username='admin', password='password')

        # Creating sample publisher
        self.publisher_data = {
            'name': 'Test Publisher',
            'address': '123 Test Street'
        }

        # Creating a sample publisher instance
        self.publisher_instance = Publisher.objects.create(
            name='Existing Publisher',
            address='456 Existing Street'
        )

    def test_publishers_list_view(self):
        response = self.client.get(reverse('admin-publishers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/publisher/publishers.html')

    def test_publishers_create_view(self):
        response = self.client.post(reverse('admin-publisher-create'), data=self.publisher_data)
        self.assertEqual(response.status_code, 302) 

        # created_publisher = Publisher.objects.get(name='Test Publisher')
        # self.assertEqual(created_publisher.address, '123 Test Street')

    def test_publisher_detail_view(self):
        response = self.client.get(reverse('admin-publisher-detail', kwargs={'pk': self.publisher_instance.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/publisher/publisher-detail.html')

    def test_publisher_delete_view(self):
        response = self.client.post(reverse('admin-publisher-delete', kwargs={'pk': self.publisher_instance.pk}))
        self.assertEqual(response.status_code, 302)  # Should redirect after successful deletion

        with self.assertRaises(Publisher.DoesNotExist):
            Publisher.objects.get(pk=self.publisher_instance.pk)

    def test_publishers_update_view(self):
        updated_data = {
            'name': 'Updated Publisher',
            'address': '789 Updated Street'
        }
        response = self.client.post(reverse('admin-publisher-update', kwargs={'pk': self.publisher_instance.pk}), data=updated_data)
        self.assertEqual(response.status_code, 302)

        # updated_publisher = Publisher.objects.get(pk=self.publisher_instance.pk)
        # self.assertEqual(updated_publisher.name, 'Updated Publisher')
        # self.assertEqual(updated_publisher.address, '789 Updated Street')
