from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.books.models import Author
from src.core.mixins import CachedViewMixin, SuperuserRequiredMixin

from ..forms import AuthorCreateForm


# AUTHOR VIEWS
class AuthorsList(SuperuserRequiredMixin, CachedViewMixin, ListView):
    model = Author
    template_name = 'store_admin/authors.html'
    paginate_by = 20


class AuthorsCreate(SuperuserRequiredMixin, CachedViewMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'store_admin/author-create.html'
    success_url = reverse_lazy('admin-authors')


class AuthorsUpdate(SuperuserRequiredMixin, CachedViewMixin, UpdateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'store_admin/author-update.html'
    success_url = reverse_lazy('admin-authors')


class AuthorDetailView(SuperuserRequiredMixin, CachedViewMixin, DetailView):
    model = Author
    template_name = 'store_admin/author-detail.html'


class AuthorDelete(SuperuserRequiredMixin, CachedViewMixin, DeleteView):
    model = Author
    success_url = reverse_lazy(
        'admin-authors'
    )  # Redirect to admin authors list after deletion
    template_name = 'store_admin/author-confirm-delete.html'
