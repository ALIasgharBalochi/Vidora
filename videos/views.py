from django.shortcuts import render
from .seiralizers import (
    VideoSerializer,
    WatchedSerializer,
    CreateCommentSerializer,
    ListCommentSerializer,
    AddLikeVideo,
    AddRatingVideo,
)
from django.db.models import Count, Avg
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Video, WatchedVideo, Comment, LikeVide, RatingVideo
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
import random
from users.permissions import PlanPermission

User = get_user_model()
# Create your views here.


class ListVideoView(ListAPIView):
    # queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Video.objects.annotate(
            like_count=Count("likes"), score=Avg("ratings__score")
        )


class DetailVideoView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated, PlanPermission]

    def get(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            user = self.request.user
            video = Video.objects.get(id=self.kwargs["pk"])
            wateched_minuts = random.randrange(0, 90)
            try:
                WatchedVideo.objects.filter(
                    user=request.user,
                    video_id=video.id,
                ).update(watched_minuts=wateched_minuts)
            except WatchedVideo.DoesNotExist:
                try:
                    WatchedVideo.objects.create(
                        user=user, video=video, watched_minuts=wateched_minuts
                    )
                except Exception as e:
                    print("fail to add to watched ")

        return super().get(request, *args, **kwargs)


class ListWatchedVideo(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchedSerializer

    def get_queryset(self):
        user = self.request.user
        return WatchedVideo.objects.filter(user=user)


class ListCommentView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListCommentSerializer

    def get_queryset(self):
        movie_id = self.kwargs["pk"]
        return Comment.objects.filter(video__id=movie_id)


class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class LikeVideoView(CreateAPIView):
    queryset = LikeVide.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AddLikeVideo

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class RatingVideoView(CreateAPIView):
    queryset = RatingVideo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AddRatingVideo

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)
