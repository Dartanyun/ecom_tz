from api_v1.views.stock import CategoryViewSet, EquipmentViewSet, StockViewSet
from api_v1.views.users import UsersViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users", UsersViewSet, basename="users")
router.register("stocks", StockViewSet, basename="stock")
router.register("equipments", EquipmentViewSet, basename="equipment")
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("v1/", include(router.urls)),
]
