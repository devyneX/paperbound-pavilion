from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import BadRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from src.accounts.forms import CustomAuthenticationForm, RegisterForm


class Login(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Get the 'next' parameter from the GET request
        next_url = self.request.GET.get('next')
        # If 'next' parameter exists, redirect to it, otherwise use LOGIN_REDIRECT_URL # noqa: E501
        if next_url:
            return next_url
        else:
            return super().get_success_url()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise BadRequest

        return super().post(self, request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, form.instance)
        return response


class Logout(LogoutView):
    next_page = reverse_lazy('accounts:login')
