from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
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
    # TODO: Doesn't redirect authenticated users
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        password = form.cleaned_data['password1']
        form.instance.set_password(password)

        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_initial_data'] = self.request.POST
        return context


class Logout(LogoutView):
    next_page = reverse_lazy('accounts:login')
