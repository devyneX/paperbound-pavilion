from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.books.models import Publisher

from ..forms import PublisherCreateForm


# PUBLISHER VIEWS
class PublishersList(PermissionRequiredMixin, ListView):
    model = Publisher
    template_name = 'store_admin/publisher/publishers.html'
    paginate_by = 20
    permission_required = ('books.view_publisher',)


class PublishersCreate(PermissionRequiredMixin, CreateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'store_admin/publisher/publisher-create.html'
    success_url = reverse_lazy('admin-publishers')
    permission_required = ('books.add_publisher',)


class PublishersUpdate(PermissionRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'store_admin/publisher/publisher-update.html'
    success_url = reverse_lazy('admin-publishers')
    permission_required = ('books.change_publisher',)


class PublisherDetailView(PermissionRequiredMixin, DetailView):
    model = Publisher
    template_name = 'store_admin/publisher/publisher-detail.html'
    permission_required = ('books.view_publisher',)


class PublisherDelete(PermissionRequiredMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy(
        'admin-publishers'
    )  # Redirect to admin publishers list after deletion
    template_name = 'store_admin/publisher/publisher-confirm-delete.html'
    permission_required = ('books.delete_publisher',)
