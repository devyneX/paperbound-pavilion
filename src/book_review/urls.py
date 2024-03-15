from django.urls import path

from .views import ReviewCreateView

app_name = 'review'

reviewurlpatterns = [
    # path(
    #     'book/<int:pk>/',
    #     BookReviewListView.as_view(),
    #     name='review_list_book'
    # ),
    # path(
    #     'user/<int:pk>/',
    #     UserReviewListView.as_view(),
    #     name='review_list_user'
    # ),
    path(
        '<int:pk>/create_review/',
        ReviewCreateView.as_view(),
        name='create_review'
    ),
    # path('update_review/',ReviewUpdateView.as_view(), name="update_view")
]
