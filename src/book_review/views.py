from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from ..core.mixins import OwnerRequiredMixin
from .forms import ReviewForm
from .models import Book, Review


class BookReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'review_list_book.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(books__id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        book = get_object_or_404(Book, pk=pk)
        context['book'] = book
        return context


class ReviewCreateView(PermissionRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create_review.html'
    success_url = reverse_lazy('book-list')
    permission_required = ('book_review.add_own_review',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.books = Book.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs.get('pk'))
        return context


class UserReviewListView(PermissionRequiredMixin, ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'review_list_user.html'
    permission_required = ('book_review.view_own_review',)

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class ReviewUpdateView(OwnerRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'update_review.html'
    success_url = reverse_lazy('book-list')
    permission_required = ('book_review.change_own_review',)

    def is_owner(self, request):
        return self.get_object().user == request.user
