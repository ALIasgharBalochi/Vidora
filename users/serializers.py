from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Plans, TransActin

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = "__all__"
        extra_kwargs = {"price": {"read_only": True}}


class TransactoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransActin
        fields = "__all__"


class SendPaymentInfor(serializers.Serializer):
    plan_id = serializers.PrimaryKeyRelatedField(queryset=Plans.objects.all())
