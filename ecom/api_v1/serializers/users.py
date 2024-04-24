from api_v1.serializers.stock import (
    EquipmentUserSerializer,
    EquipmentUserShortSerializer,
)
from core.validators import validate_equipments
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer
from stock.models import Equipment, EquipmentUser
from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор пользователя.
    """

    equipments = EquipmentUserSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "middle_name",
            "equipments",
        )


class UserCreateSerializer(ModelSerializer):
    """
    Сериализатор создания экземпляра пользователя.
    """

    equipments = EquipmentUserShortSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "middle_name",
            "password",
            "equipments",
        )

    def validate_password(self, data):
        validate_password(data, User)
        return data

    def validate(self, data):
        return validate_equipments(self, data)

    def create(self, validated_data):
        equipments_data = validated_data.pop("equipments")
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)

        self.update_or_create_equipment_users(user, equipments_data)

        return user

    def update(self, instance, validated_data):
        if "equipments" in validated_data:
            equipments_data = validated_data.pop("equipments")
            EquipmentUser.objects.filter(user=instance).delete()

        self.update_or_create_equipment_users(instance, equipments_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def update_or_create_equipment_users(self, user, equipments_data):
        """
        Создает новые записи в связанной таблице EquipmentUser.
        """

        data = [
            EquipmentUser(
                equipment=get_object_or_404(
                    Equipment, id=equipment_data["equipment"]["id"]
                ),
                quantity=equipment_data["quantity"],
                user=user,
            )
            for equipment_data in equipments_data
        ]

        EquipmentUser.objects.bulk_create(data)

    def to_representation(self, instance):
        return UserSerializer(instance).data
