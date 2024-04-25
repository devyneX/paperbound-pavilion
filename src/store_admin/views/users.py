from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.accounts.models import User

from ..forms import UserCreateForm


# USER VIEWS
class UsersList(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'store_admin/user/users.html'
    paginate_by = 20
    permission_required = ('accounts.view_user',)


class UsersCreate(PermissionRequiredMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'store_admin/user/user-create.html'
    success_url = reverse_lazy('admin-users')
    permission_required = ('accounts.add_user',)

    def form_valid(self, form):
        password = form.cleaned_data['password']
        form.instance.set_password(password)

        form.save()

        return super().form_valid(form)


class UsersUpdate(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'store_admin/user/user-update.html'
    success_url = reverse_lazy('admin-users')
    permission_required = ('accounts.change_user',)


class UserDetailView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'store_admin/user/user-detail.html'
    permission_required = ('accounts.view_user',)


class UserDelete(PermissionRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy(
        'admin-users'
    )  # Redirect to admin users list after deletion
    template_name = 'store_admin/user/user-confirm-delete.html'
    permission_required = ('accounts.delete_user',)
