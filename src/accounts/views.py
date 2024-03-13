from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomAuthenticationForm, RegisterForm


class Login(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
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
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Hash the password before saving
        form.instance.set_password(form.cleaned_data['password'])
        return super().form_valid(form)


class Logout(LogoutView):
    next_page = reverse_lazy('login')
