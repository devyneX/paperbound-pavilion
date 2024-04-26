from django.test import Client, TestCase

from src.accounts.models import User


class TestDashboard(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin',
            phone='1234567890'
        )

    def test_dashboard(self):
        self.client.force_login(self.user)
        response = self.client.get('/djadmin/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/index.html')
