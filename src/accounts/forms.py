# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


# FIXME: need to add phone field and validate that it's within 20 characters
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
