from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User
from reviews.serializers import ReviewSerializer


class PublicUserSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "avatar",
            "email",
            "gender",
            "reviews",
        )


class PrivateUserSerializer(ModelSerializer):
    # reviews = SerializerMethodField()
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
            "name",
            "email",
            "is_host",
            "gender",
            "language",
            "currency",
        )


class TinyUserSerializer(ModelSerializer):
    # reviews = ReviewSerializer()
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )
