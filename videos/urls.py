from django.urls import path
from .views import (
    ListVideoView,
    ListCommentView,
    CreateCommentView,
    ListWatchedVideo,
    DetailVideoView,
    LikeVideoView,
    RatingVideoView,
)

urlpatterns = [
    path("", ListVideoView.as_view(), name="videos"),
    path("comments/<int:pk>/", ListCommentView.as_view(), name="comments"),
    path("add_comments/", CreateCommentView.as_view(), name="add_comments"),
    path("watched_videos/", ListWatchedVideo.as_view(), name="watched_videos"),
    path("move_detail/<int:pk>/", DetailVideoView.as_view(), name="movie_detail"),
    path("like/", LikeVideoView.as_view(), name="like_video"),
    path("rating/", RatingVideoView.as_view(), name="rate_video"),
]
