from rest_framework import serializers
from .models import Video, Comment, WatchedVideo, LikeVide, RatingVideo


class VideoSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    score = serializers.FloatField(read_only=True)

    class Meta:
        model = Video
        fields = ["url", "like_count", "score"]


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


class AddLikeVideo(serializers.ModelSerializer):

    class Meta:
        model = LikeVide
        fields = ["user", "video"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        return LikeVide.objects.create(**validated_data)


class AddRatingVideo(serializers.ModelSerializer):
    video = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all())
    score = serializers.FloatField()

    class Meta:
        model = RatingVideo
        fields = ["user", "video", "score"]
        read_only_fields = ["user"]

    def validate_score(self, value):
        if not 0.0 <= value <= 5.0:
            raise serializers.ValidationError("the score shold be betwen 0 and 5")
        return value

    def create(self, validated_data):
        return RatingVideo.objects.create(**validated_data)
