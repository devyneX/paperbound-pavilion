from django.views.generic import ListView, TemplateView

from src.books.models import Book
from src.core.mixins import SuperuserRequiredMixin


class AdminDashboard(TemplateView):
    template_name = 'store_admin/dashboard.html'


class BooksList(SuperuserRequiredMixin, ListView):
    model = Book
    template_name = 'store_admin/books.html'
    paginate_by = 20
