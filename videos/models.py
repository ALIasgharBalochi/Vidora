from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Video(models.Model):
    url = models.CharField()
    like_count = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="comments")
    video = models.ForeignKey(Video, models.CASCADE, related_name="comments")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class WatchedVideo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="watched_videos"
    )
    video = models.ForeignKey(Video, related_name="watched_videos")
    watched_minuts = models.IntegerField()
