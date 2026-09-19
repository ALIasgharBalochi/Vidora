from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Video(models.Model):
    plane_choises = [("bronze", "Bronze"), ("silver", "Silver"), ("gold", "Gold")]
    url = models.CharField()
    required_plan = models.CharField(choices=plane_choises)

    def __str__(self):
        return self.url


class LikeVide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["user", "video"],
                name="unique_like_user_video",
            )
        ]


class RatingVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="ratings")
    score = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ],
    )

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["user", "video"],
                name="unique_rating_user_video",
            )
        ]


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="comments")
    video = models.ForeignKey(Video, models.CASCADE, related_name="comments")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class WatchedVideo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="watched_videos"
    )
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name="watched_videos"
    )
    watched_minuts = models.IntegerField()

    def __str__(self):
        return self.user.username
