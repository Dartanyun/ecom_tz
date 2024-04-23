from api_v1.serializers.stock import (
    CategorySerializer,
    EquipmentSerializer,
    StockSerializer,
)
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from stock.models import Category, Equipment, Stock

User = get_user_model()


class StockViewSet(ModelViewSet):
    """ "
    ViewSet модели Stock.
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (AllowAny,)


class CategoryViewSet(ModelViewSet):
    """
    ViewSet модели Category.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class EquipmentViewSet(ModelViewSet):
    """
    ViewSet модели Equipment
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (AllowAny,)
