from django.contrib.auth.forms import AuthenticationForm

from src.accounts.models import User


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
