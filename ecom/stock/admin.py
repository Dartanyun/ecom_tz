from django.contrib import admin
from stock.models import (
    Category,
    Equipment,
    EquipmentStock,
    EquipmentUser,
    Stock,
)


class EquipmentUserTabularInline(admin.TabularInline):
    model = EquipmentUser


class EquipmentStockTabularInline(admin.TabularInline):
    model = EquipmentStock


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "description",
    )
    search_fields = ("name", "category")
    list_filter = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "description")
    search_fields = ("name", "address")
    inlines = [EquipmentStockTabularInline]
