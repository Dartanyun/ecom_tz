from api_v1.serializers.stock import (
    CategorySerializer,
    EquipmentCreateSerializer,
    EquipmentSerializer,
    StockCreateSerializer,
    StockSerializer,
)
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from stock.models import Category, Equipment, Stock

User = get_user_model()


class StockViewSet(ModelViewSet):
    """
    ViewSet модели Stock.
    """

    queryset = Stock.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StockSerializer
        return StockCreateSerializer


class CategoryViewSet(ModelViewSet):
    """
    ViewSet модели Category.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EquipmentViewSet(ModelViewSet):
    """
    ViewSet модели Equipment
    """

    queryset = Equipment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EquipmentSerializer
        return EquipmentCreateSerializer
