from django.urls import path

from .views import (
    FeedListView,
    UserDetailView,
    FollowView,
    UnfollowView,
)


urlpatterns = [
    path('u/<slug>/unfollow/', UnfollowView.as_view(), name='unfollow-user'),
    path('u/<slug>/follow/', FollowView.as_view(), name='follow-user'),
    path('u/<slug>/', UserDetailView.as_view(), name='user-detail'),
    path('', FeedListView.as_view(), name='feed-list'),
]
