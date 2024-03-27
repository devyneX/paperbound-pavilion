from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.accounts.models import User
from src.core.mixins import CachedViewMixin, SuperuserRequiredMixin

from ..forms import UserCreateForm


# USER VIEWS
class UsersList(SuperuserRequiredMixin, CachedViewMixin, ListView):
    model = User
    template_name = 'store_admin/user/users.html'
    paginate_by = 20


class UsersCreate(SuperuserRequiredMixin, CachedViewMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'store_admin/user/user-create.html'
    success_url = reverse_lazy('admin-users')

    def form_valid(self, form):
        password = form.cleaned_data['password']
        form.instance.set_password(password)

        form.save()

        return super().form_valid(form)


class UsersUpdate(SuperuserRequiredMixin, CachedViewMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'store_admin/user/user-update.html'
    success_url = reverse_lazy('admin-users')


class UserDetailView(SuperuserRequiredMixin, CachedViewMixin, DetailView):
    model = User
    template_name = 'store_admin/user/user-detail.html'


class UserDelete(SuperuserRequiredMixin, CachedViewMixin, DeleteView):
    model = User
    success_url = reverse_lazy(
        'admin-users'
    )  # Redirect to admin users list after deletion
    template_name = 'store_admin/user/user-confirm-delete.html'
