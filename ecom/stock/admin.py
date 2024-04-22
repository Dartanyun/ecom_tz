from django.contrib import admin
from stock.models import Category, Equipment, Stock


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "stock",
        "description",
        "quantity",
    )
    search_fields = ("name", "category", "stock")
    list_filter = ("name", "category", "stock")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "description")
    search_fields = ("name", "address")
