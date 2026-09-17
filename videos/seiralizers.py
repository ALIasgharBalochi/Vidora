from rest_framework import serializers
from .models import Video, Comment, WatchedVideo


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all___"

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class WatchedSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchedVideo
        fields = "__all__"
