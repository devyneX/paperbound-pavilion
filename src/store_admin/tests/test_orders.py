from django.test import Client, TestCase
from django.urls import reverse

from src.accounts.models import User
from src.shopping.models import Address, Order, OrderStatusChoices


class TestOrderViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.login(username='admin', password='password')

        # Creating sample address
        self.address = Address.objects.create(
            user=self.user,
            house='123',
            street='Test Street',
            city='Test City',
            country='US',
            post_code='12345'
        )

        # Creating sample order
        self.order = Order.objects.create(
            user=self.user,
            address=self.address,
            status=OrderStatusChoices.PENDING
        )

    def test_orders_list_view(self):
        response = self.client.get(reverse('admin-orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_admin/order/orders.html')

    def test_orders_update_view(self):
        response = self.client.get(
            reverse('admin-order-update', kwargs={'pk': self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'store_admin/order/order-update.html'
        )

        # Test updating order with valid data
        updated_data = {
            'user': self.user.id,
            'address': self.address.id,
            'status': OrderStatusChoices.PROCESSING,
            'books': '[]'
        }
        response = self.client.post(
            reverse('admin-order-update', kwargs={'pk': self.order.pk}),
            data=updated_data
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful update

        # updated_order = Order.objects.get(pk=self.order.pk)
        # self.assertEqual(updated_order.status, OrderStatusChoices.PROCESSING)

    def test_order_detail_view(self):
        response = self.client.get(
            reverse('admin-order-detail', kwargs={'pk': self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'store_admin/order/order-detail.html'
        )

    def test_order_delete_view(self):
        response = self.client.post(
            reverse('admin-order-delete', kwargs={'pk': self.order.pk})
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful deletion

        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(pk=self.order.pk)
