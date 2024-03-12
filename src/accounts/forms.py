# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'password', 'username'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
