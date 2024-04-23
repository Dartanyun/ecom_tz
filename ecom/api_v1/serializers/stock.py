from rest_framework.serializers import ModelSerializer
from stock.models import Category, Equipment, Stock


class CategorySerializer(ModelSerializer):
    """
    Сериализатор модели Category.
    """

    class Meta:
        model = Category
        fields = ("id", "name", "description")


class StockSerializer(ModelSerializer):
    """
    Сериализатор модели Stock.
    """

    class Meta:
        model = Stock
        fields = ("id", "name", "address", "description")


class EquipmentSerializer(ModelSerializer):
    """
    Сериализатор модели Equipment.
    """

    category = CategorySerializer()
    stock = StockSerializer()

    class Meta:
        model = Equipment
        fields = ("id", "name", "description", "category", "stock", "quantity")
