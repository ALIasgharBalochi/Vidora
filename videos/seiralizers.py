from rest_framework import serializers
from .models import Video, Comment, WatchedVideo


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"


class ListCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CreateCommentSerializer(serializers.Serializer):
    video = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all())
    message = serializers.CharField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class WatchedSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchedVideo
        fields = "__all__"
