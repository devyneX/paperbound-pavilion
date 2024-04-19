from django.contrib.auth.hashers import make_password
from django.test import Client, TestCase
from django.urls import reverse
from faker import Faker

from src.accounts.forms import CustomAuthenticationForm, RegisterForm
from src.accounts.tests.utils import make_fake_user

fake = Faker()


class LoginViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_unauthenticated_user(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(
            response.context['form'], CustomAuthenticationForm
        )

    def test_get_authenticated_user(self):
        user = make_fake_user(fake)
        self.client.force_login(user)
        response = self.client.get(reverse('accounts:login'))
        self.assertRedirects(response, reverse('home'))

    def test_post_authenticated_user(self):
        password = fake.password()
        hashed_password = make_password(password)
        user = make_fake_user(fake, password=hashed_password)

        self.client.force_login(user)

        data = {
            'username': user.username,
            'password': password,
        }

        response = self.client.post(reverse('accounts:login'), data)

        self.assertRedirects(response, reverse('home'))

        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_valid_login(self):
        password = fake.password()
        hashed_password = make_password(password)
        user = make_fake_user(fake, password=hashed_password)
        data = {
            'username': user.username,
            'password': password,
        }
        response = self.client.post(reverse('accounts:login'), data)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_login(self):
        user = make_fake_user(fake)
        data = {
            'username': user.username,
            'password': 'invalid_password',
        }
        response = self.client.post(reverse('accounts:login'), data)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class LogoutViewTests(TestCase):

    def setUp(self):
        self.password = 'password1234'
        self.user = make_fake_user(fake)
        self.client = Client()

    def test_valid_logout(self):
        self.client.login(username=self.user.username, password=self.password)

        response = self.client.post(reverse('accounts:logout'), {})

        self.assertRedirects(response, reverse('accounts:login'))

        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_invalid_logout(self):
        response = self.client.post(reverse('accounts:logout'), {})

        self.assertRedirects(response, reverse('accounts:login'))

        self.assertFalse(response.wsgi_request.user.is_authenticated)


class RegistrationViewTests(TestCase):

    def setUp(self):
        pass

    def test_valid_registration(self):
        password = fake.password()
        data = {
            'username': fake.user_name(),
            'email': fake.email(),
            'password1': password,
            'password2': password,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'phone_number': fake.random_number(digits=20),
        }

        response = self.client.post(reverse('accounts:register'), data)
        print(response)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_registration(self):
        data = {
            'username': '',
            'email': 'invalid-email',
            'password1': 'password123',
            'password2': '',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890'
        }

        response = self.client.post(reverse('accounts:register'), data)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_get_registration_authenticated(self):
        user = make_fake_user(fake)
        self.client.force_login(user)
        response = self.client.get(reverse('accounts:register'))
        self.assertRedirects(response, reverse('home'))

    def test_get_registration_unauthenticated(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)

    def test_post_registration_authenticated(self):
        user = make_fake_user(fake)
        self.client.force_login(user)

        data = {
            'username': '',
            'email': 'invalid-email',
            'password1': 'password123',
            'password2': 'password123',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890'
        }

        response = self.client.post(reverse('accounts:register'), data)

        self.assertEqual(response.status_code, 400)
