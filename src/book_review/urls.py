from django.urls import path

from .views import (
    BookReviewListView, ReviewCreateView, ReviewUpdateView, UserReviewListView
)

app_name = 'review'

urlpatterns = [
    path('<int:pk>/', BookReviewListView.as_view(), name='reviews'),
    path(
        'user/<str:username>/',
        UserReviewListView.as_view(),
        name='user-reviews'
    ),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='update-review'),
    path('<int:pk>/create/', ReviewCreateView.as_view(), name='create-review'),
    # path('update_review/',ReviewUpdateView.as_view(), name="update_view")
]
