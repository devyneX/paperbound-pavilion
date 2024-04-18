from django.test import Client, TestCase
from django.urls import reverse

from src.accounts.models import User


class TestUserViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.login(username='admin', password='password')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        self.user_update_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password': 'updatedpassword'
        }
        self.user_instance = User.objects.create_user(
            username='existinguser',
            email='existinguser@example.com',
            password='existingpassword'
        )

    def test_users_list_view(self):
        response = self.client.get(reverse('admin-users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/user/users.html')

    def test_users_create_view(self):
        response = self.client.post(
            reverse('admin-user-create'), data=self.user_data
        )
        self.assertEqual(response.status_code, 200)

        # created_user = User.objects.get(username='testuser')
        # self.assertEqual(created_user.email, 'testuser@example.com')

    def test_users_update_view(self):
        response = self.client.post(
            reverse('admin-user-update', kwargs={'pk': self.user_instance.pk}),
            data=self.user_update_data
        )
        self.assertEqual(response.status_code, 200)

        # updated_user = User.objects.get(pk=self.user_instance.pk)
        # self.assertEqual(updated_user.username, 'updateduser')
        # self.assertEqual(updated_user.email, 'updateduser@example.com')

    def test_user_detail_view(self):
        response = self.client.get(
            reverse('admin-user-detail', kwargs={'pk': self.user_instance.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/user/user-detail.html')

    def test_user_delete_view(self):
        response = self.client.post(
            reverse('admin-user-delete', kwargs={'pk': self.user_instance.pk})
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful deletion

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user_instance.pk)
