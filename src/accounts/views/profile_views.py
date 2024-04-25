from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from src.accounts.models import Address, User
from src.core.mixins import OwnerRequiredMixin


class SelfProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/self-profile.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)


class ProfileView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
    permission_required = ('accounts.view_profile',)

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get(self, request, *args, **kwargs):
        if request.user.username == self.get_object().username:
            return redirect('accounts:self-profile')
        return super().get(request, *args, **kwargs)


class ProfileUpdateView(OwnerRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'accounts/profile-update.html'
    success_url = reverse_lazy('accounts:self-profile')
    permission_required = ('accounts.change_own_profile',)

    def is_owner(self, request):
        return self.request.user.username == self.get_object().username

    def get_object(self):
        return self.request.user


class AddressListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'accounts/address-list.html'
    context_object_name = 'addresses'
    permission_required = ('accounts.view_own_address',)

    def get_queryset(self):
        return self.request.user.addresses.all()


class AddressCreateView(PermissionRequiredMixin, CreateView):
    model = Address
    fields = ['house', 'street', 'city', 'state', 'post_code', 'country']
    template_name = 'accounts/address-create.html'
    success_url = reverse_lazy('accounts:address-list')
    permission_required = ('accounts.add_own_address',)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressUpdateView(OwnerRequiredMixin, UpdateView):
    model = Address
    template_name = 'accounts/address-update.html'
    fields = ['house', 'street', 'city', 'state', 'post_code', 'country']
    success_url = reverse_lazy('accounts:address-list')
    permission_required = ('accounts.change_own_address',)

    def is_owner(self, request):
        return self.request.user == self.get_object().user

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])
