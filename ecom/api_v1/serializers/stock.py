from core.validators import validate_equipments
from django.shortcuts import get_object_or_404
from rest_framework.serializers import IntegerField, ModelSerializer
from stock.models import (
    Category,
    Equipment,
    EquipmentStock,
    EquipmentUser,
    Stock,
)


class CategorySerializer(ModelSerializer):
    """
    Сериализатор модели Category.
    """

    class Meta:
        model = Category
        fields = ("id", "name", "description")


class EquipmentSerializer(ModelSerializer):
    """
    Сериализатор модели Equipment.
    """

    category = CategorySerializer()

    class Meta:
        model = Equipment
        fields = ("id", "name", "description", "category")


class EquipmentCreateSerializer(ModelSerializer):
    """
    Сериализатор создания экземпляра модели Equipment.
    """

    category = IntegerField(source="category.id")

    class Meta:
        model = Equipment
        fields = ("id", "name", "description", "category")

    def create(self, validated_data):
        category_data = validated_data.pop("category")["id"]
        equipment = Equipment.objects.create(
            **validated_data,
            category=get_object_or_404(Category, id=category_data)
        )
        return equipment

    def update(self, instance, validated_data):
        if "category" in validated_data:
            category_data = validated_data.pop("category")["id"]
            instance.category = get_object_or_404(Category, id=category_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        return instance

    def to_representation(self, instance):
        return EquipmentSerializer(instance).data


class EquipmentStockSerializer(ModelSerializer):
    """
    Сериализатор связанной модели EquipmentStock.
    """

    equipment = EquipmentSerializer()

    class Meta:
        model = EquipmentStock
        fields = ("equipment", "quantity")


class EquipmentStockShortSerializer(ModelSerializer):
    """
    Укороченный сериализатор связанной модели EquipmentStock.
    Используется в StockSerializer при создании записей.
    """

    equipment = IntegerField(source="equipment.id")

    class Meta:
        model = EquipmentStock
        fields = ("equipment", "quantity")


class StockSerializer(ModelSerializer):
    """
    Сериализатор модели Stock.
    """

    equipments = EquipmentStockSerializer(many=True)

    class Meta:
        model = Stock
        fields = ("id", "name", "address", "description", "equipments")


class StockCreateSerializer(ModelSerializer):
    """
    Сериализатор создания экземпляра модели Stock.
    """

    equipments = EquipmentStockShortSerializer(many=True)

    class Meta:
        model = Stock
        fields = ("id", "name", "address", "description", "equipments")

    def validate(self, data):
        return validate_equipments(self, data)

    def create(self, validated_data):
        equipments_data = validated_data.pop("equipments")
        stock = Stock.objects.create(**validated_data)

        self.update_or_create_equipment_stock(stock, equipments_data)

        return stock

    def update(self, instance, validated_data):
        if "equipments" in validated_data:
            equipments_data = validated_data.pop("equipments")
            EquipmentStock.objects.filter(stock=instance).delete()

        self.update_or_create_equipment_stock(instance, equipments_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def update_or_create_equipment_stock(self, stock, equipments_data):
        data = [
            EquipmentStock(
                equipment=get_object_or_404(
                    Equipment, id=equipment_data["equipment"]["id"]
                ),
                quantity=equipment_data["quantity"],
                stock=stock,
            )
            for equipment_data in equipments_data
        ]

        EquipmentStock.objects.bulk_create(data)

    def to_representation(self, instance):
        return StockSerializer(instance).data


class EquipmentUserSerializer(ModelSerializer):
    """
    Сериализатор связанной модели EquipmentUser.
    Используется в UserSerializer.
    """

    equipment = EquipmentSerializer()

    class Meta:
        model = EquipmentUser
        fields = ("equipment", "quantity")


class EquipmentUserShortSerializer(ModelSerializer):
    """
    Укороченный сериализатор связанной модели EquipmentUser.
    Используется в UserCreateSerializer при создании записей.
    """

    equipment = IntegerField(source="equipment.id")

    class Meta:
        model = EquipmentUser
        fields = ("equipment", "quantity")
