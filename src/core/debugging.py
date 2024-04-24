import django
from django.conf import settings
from django.test import Client
from django.urls import reverse
from faker import Faker

fake = Faker()

settings.configure(DEBUG=True)
django.setup()

client = Client()

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

response = client.post(reverse('accounts:register'), data)
print(response)
