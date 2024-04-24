from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.books.models import Author

from ..forms import AuthorCreateForm


# AUTHOR VIEWS
class AuthorsList(PermissionRequiredMixin, ListView):
    model = Author
    template_name = 'store_admin/author/authors.html'
    paginate_by = 20
    permission_required = ('books.view_author',)


class AuthorsCreate(PermissionRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'store_admin/author/author-create.html'
    success_url = reverse_lazy('admin-authors')
    permission_required = ('books.add_author',)


class AuthorsUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'store_admin/author/author-update.html'
    success_url = reverse_lazy('admin-authors')
    permission_required = ('books.change_author',)


class AuthorDetailView(PermissionRequiredMixin, DetailView):
    model = Author
    template_name = 'store_admin/author/author-detail.html'
    permission_required = ('books.view_author',)


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy(
        'admin-authors'
    )  # Redirect to admin authors list after deletion
    template_name = 'store_admin/author/author-confirm-delete.html'
    permission_required = ('books.delete_author',)
