from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

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
        context['book_title'] = book.title
        return context


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create_review.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.books = Book.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs.get('pk'))
        return context


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'update_review.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)
