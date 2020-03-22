from django.urls import path

from .views import (
    FeedListView,
    UserDetailView,
    FollowView,
    UnfollowView,
    MarkReadView,
    UnmarkReadView,
)


urlpatterns = [
    path(
        'post/<pk>/unmark-read/',
        UnmarkReadView.as_view(),
        name='post-unmark-read'
    ),
    path(
        'post/<pk>/mark-read/',
        MarkReadView.as_view(),
        name='post-mark-read'
    ),
    path('u/<slug>/unfollow/', UnfollowView.as_view(), name='unfollow-user'),
    path('u/<slug>/follow/', FollowView.as_view(), name='follow-user'),
    path('u/<slug>/', UserDetailView.as_view(), name='user-detail'),
    path('', FeedListView.as_view(), name='feed-list'),
]
