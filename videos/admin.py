from django.contrib import admin
from .models import Video, Comment, WatchedVideo

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class VideoComments(admin.ModelAdmin):
    pass


@admin.register(WatchedVideo)
class VideoWatchedVideo(admin.ModelAdmin):
    pass
