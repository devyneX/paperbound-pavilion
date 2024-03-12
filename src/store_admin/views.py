from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from .forms import CustomAuthenticationForm


class AdminLogin(View):
    template_name = 'store_admin/login.html'
    auth_form = CustomAuthenticationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.auth_form(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                form.add_error(
                    None, 'You are not authorized to access this page.'
                )

        return render(request, self.template_name, {'form': form})
