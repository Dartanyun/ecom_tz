from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор пользователя.
    """

    class Meta:
        model = User
        fields = ("username",)


class UserCreateSerializer(ModelSerializer):
    """
    Сериализатор создания пользователя.
    """

    class Meta:
        model = User
        fields = ("username", "password")

    def validate_password(self, data):
        validate_password(data, User)
        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
