# from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker

from src.accounts.forms import CustomAuthenticationForm, RegisterForm
from src.accounts.tests.utils import make_fake_user

fake = Faker()


class RegisterFormTestCase(TestCase):

    def setUp(self):
        password = fake.password()
        self.form_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'username': fake.user_name(),
            'password1': password,
            'password2': password,
            'phone': fake.random_number(digits=20),
        }

    def test_valid_registration(self):
        form = RegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_password_match(self):
        self.form_data.update({
            'password1': 'password123',
            'password2': 'different password'
        })
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match', form.errors['password2'])

    def test_invalid_missing_fields(self):
        form_data = {}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        # self.assertIn('first_name', form.errors)
        # self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone', form.errors)
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    def test_duplicate_email(self):
        user = make_fake_user(fake)
        self.form_data.update({'email': user.email})
        form = RegisterForm(data=self.form_data)

        self.assertFalse(form.is_valid())
        self.assertIn(
            'User with this Email already exists.', form.errors['email']
        )

    def test_duplicate_username(self):
        user = make_fake_user(fake, username=fake.user_name())
        self.form_data.update({'username': user.username})
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            'A user with that username already exists.',
            form.errors['username']
        )


class CustomAuthenticationFormTestCase(TestCase):

    def setUp(self):
        self.password = 'password123'
        self.user = make_fake_user(fake, password=self.password)
        # print(self.user.username, self.password)

    def test_valid_authentication(self):
        form_data = {
            'username': self.user.username,
            'password': 'password123',
        }

        form = CustomAuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_wrong_password(self):
        form_data = {
            'username': self.user.username,
            'password': '<PASSWORD>',
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_username(self):
        form_data = {
            'username': 'username',
            'password': '<PASSWORD>',
        }
        form = CustomAuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid())
