from django.urls import path

from .views import BookReviewListView, ReviewCreateView, ReviewUpdateView

app_name = 'review'

reviewurlpatterns = [
    path('<int:pk>/reviews/', BookReviewListView.as_view(), name='reviews'),
    path(
        '<int:pk>/update_review/',
        ReviewUpdateView.as_view(),
        name='update-review'
    ),
    path(
        '<int:pk>/create_review/',
        ReviewCreateView.as_view(),
        name='create-review'
    ),
    # path('update_review/',ReviewUpdateView.as_view(), name="update_view")
]
