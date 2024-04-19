from django.db import DataError, IntegrityError
from django.test import TestCase
from faker import Faker

from src.accounts.models import Address, User

from .utils import make_fake_address, make_fake_user

fake = Faker()


class UserCreationTestCase(TestCase):

    def test_valid_basic_user_creation(self):
        user = make_fake_user(fake)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_unique_username_constraint(self):
        username = fake.user_name()
        make_fake_user(fake, username=username)
        with self.assertRaises(IntegrityError):
            make_fake_user(fake, username=username)

    def test_unique_email_constraint(self):
        email = fake.email()
        make_fake_user(fake, email=email)
        with self.assertRaises(IntegrityError):
            make_fake_user(fake, email=email)

    def test_phone_digit_constraint(self):

        phone = fake.random_number(digits=20)
        try:
            make_fake_user(fake, phone=phone)
        except Exception:
            self.fail('Phone digits constraint failed')

        phone = fake.random_number(digits=20, fix_len=True)
        try:
            make_fake_user(fake, phone=phone)

        except Exception:
            self.fail('Phone digits constraint failed')

        with self.assertRaises(DataError):
            phone = fake.random_number(digits=30, fix_len=True)
            make_fake_user(fake, phone=phone)


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = make_fake_user(fake)

    def test_user_retrieval_with_id(self):
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user, self.user)

    def test_user_retrieval_with_username(self):
        user = User.objects.get(username=self.user.username)
        self.assertEqual(user, self.user)

    def test_user_retrieval_with_email(self):
        user = User.objects.get(email=self.user.email)
        self.assertEqual(user, self.user)

    def test_user_update_name(self):
        new_first_name = fake.first_name()
        self.user.first_name = new_first_name
        self.user.save()
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.first_name, new_first_name)

        new_last_name = fake.last_name()
        self.user.last_name = new_last_name
        self.user.save()
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.last_name, new_last_name)

    def test_user_update_phone(self):
        new_phone = fake.random_number(digits=20)
        new_phone = str(new_phone)
        self.user.phone = new_phone
        self.user.save()
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.phone, new_phone)

        new_phone = fake.random_number(digits=20, fix_len=True)
        new_phone = str(new_phone)
        self.user.phone = new_phone
        self.user.save()
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.phone, new_phone)

        new_phone = fake.random_number(digits=30, fix_len=True)
        new_phone = str(new_phone)
        with self.assertRaises(DataError):
            self.user.phone = new_phone
            self.user.save()

    def test_user_update_duplicate_email(self):
        email = fake.email()
        make_fake_user(fake, email=email)
        with self.assertRaises(IntegrityError):
            self.user.email = email
            self.user.save()

    def test_user_update_duplicate_username(self):
        username = fake.user_name()
        make_fake_user(fake, username=username)
        with self.assertRaises(IntegrityError):
            self.user.username = username
            self.user.save()

    def test_user_delete(self):
        self.user.delete()
        with self.assertRaises(self.user.DoesNotExist):
            User.objects.get(id=self.user.id)

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), self.user.username)


class AddressCreationTestCase(TestCase):

    def setUp(self):
        self.user = make_fake_user(fake)

    def test_valid_address_creation(self):
        address = make_fake_address(fake, self.user)
        self.assertEqual(address.user, self.user)

        address = make_fake_address(fake, self.user, state=None)
        self.assertEqual(address.user, self.user)


class AddressModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            username=fake.user_name(),
            password=fake.password(),
            phone=fake.random_number(digits=20)
        )
        self.address = make_fake_address(fake, self.user)

    def test_address_retrieval_with_id(self):
        address = Address.objects.get(id=self.address.id)
        self.assertEqual(address, self.address)

    def test_address_retrieval_with_user(self):
        addresses = Address.objects.filter(user=self.user)
        self.assertTrue(self.address in addresses)

    def test_address_update(self):
        new_house = fake.building_number()
        self.address.house = new_house
        self.address.save()
        address = self.user.addresses.get(id=self.address.id)
        self.assertEqual(address.house, new_house)

        new_street = fake.street_name()
        self.address.street = new_street
        self.address.save()
        address = self.user.addresses.get(id=self.address.id)
        self.assertEqual(address.street, new_street)

        new_city = fake.city()
        self.address.city = new_city
        self.address.save()
        address = self.user.addresses.get(id=self.address.id)
        self.assertEqual(address.city, new_city)

        new_state = fake.state()
        self.address.state = new_state
        self.address.save()
        address = self.user.addresses.get(id=self.address.id)
        self.assertEqual(address.state, new_state)

        new_country = fake.country_code()
        self.address.country = new_country
        self.address.save()
        address = self.user.addresses.get(id=self.address.id)
        self.assertEqual(address.country, new_country)

        new_post_code = fake.postcode()
        self.address.post_code = new_post_code
        self.address.save()
        address = self.user.addresses.get(id=self.address.id)
        self.assertEqual(address.post_code, new_post_code)

    def test_address_delete(self):
        self.address.delete()
        with self.assertRaises(self.address.DoesNotExist):
            self.user.addresses.get(id=self.address.id)

    def test_address_str_representation(self):
        address = self.address
        self.assertEqual(
            str(address), f'{address.house}, {address.street}' +
            f', {address.get_country_display()}'
        )