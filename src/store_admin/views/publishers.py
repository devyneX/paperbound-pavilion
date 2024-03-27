from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from src.books.models import Publisher
from src.core.mixins import CachedViewMixin, SuperuserRequiredMixin

from ..forms import PublisherCreateForm


# PUBLISHER VIEWS
class PublishersList(SuperuserRequiredMixin, CachedViewMixin, ListView):
    model = Publisher
    template_name = 'store_admin/publisher/publishers.html'
    paginate_by = 20


class PublishersCreate(SuperuserRequiredMixin, CachedViewMixin, CreateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'store_admin/publisher/publisher-create.html'
    success_url = reverse_lazy('admin-publishers')


class PublishersUpdate(SuperuserRequiredMixin, CachedViewMixin, UpdateView):
    model = Publisher
    form_class = PublisherCreateForm
    template_name = 'store_admin/publisher/publisher-update.html'
    success_url = reverse_lazy('admin-publishers')


class PublisherDetailView(SuperuserRequiredMixin, CachedViewMixin, DetailView):
    model = Publisher
    template_name = 'store_admin/publisher/publisher-detail.html'


class PublisherDelete(SuperuserRequiredMixin, CachedViewMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy(
        'admin-publishers'
    )  # Redirect to admin publishers list after deletion
    template_name = 'store_admin/publisher/publisher-confirm-delete.html'
