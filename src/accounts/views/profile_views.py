from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from src.accounts.models import Address, User


class SelfProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/self-profile.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)


class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get(self, request, *args, **kwargs):
        if request.user.username == self.get_object().username:
            return redirect('accounts:self-profile')
        return super().get(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'accounts/profile-update.html'

    def get_object(self):
        return self.request.user


class AddressListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/address-list.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        return self.request.user.addresses.all()


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['house', 'street', 'city', 'state', 'post_code', 'country']
    template_name = 'accounts/address-create.html'
    success_url = reverse_lazy('accounts:address-list')

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    template_name = 'accounts/address-update.html'
    fields = ['house', 'street', 'city', 'state', 'post_code', 'country']
    success_url = reverse_lazy('accounts:address-list')

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])
