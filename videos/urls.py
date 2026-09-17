from django.urls import path
from .views import ListVideoView, ListCommentView, CreateCommentView, ListWatchedVideo

urlpatterns = [
    path("", ListVideoView.as_view(), name="videos"),
    path("comments/<int:pk>/", ListCommentView.as_view(), name="comments"),
    path("add_comments/", CreateCommentView.as_view(), name="add_comments"),
    path("watched_videos/", ListWatchedVideo.as_view(), name="watched_videos"),
]
