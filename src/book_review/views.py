from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Book, Review


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


# class ReviewUpdateView(UpdateView):
#     model = Review
#     form_class = ReviewForm
#     #template_name = '
#     success_url = reverse_lazy('book_list')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class BookReviewListView(ListView):
#     model = Review
#     context_object_name = 'reviews'
#     template_name = 'review_list_book.html'

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         book = get_object_or_404(Book, pk=pk)
#         return Review.objects.filter(books=book)

# class UserReviewListView(ListView):
#     model = Review
#     context_object_name = 'reviews'
#     template_name = 'review_list_user.html'

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         user = get_object_or_404(Review, pk=pk)
#         return Review.objects.filter(user=user.user)
