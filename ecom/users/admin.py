from django.contrib import admin
from django.contrib.auth.hashers import make_password
from stock.admin import EquipmentUserTabularInline
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админ панель модели пользователей.
    """

    list_display = (
        "id",
        "username",
        "last_name",
        "first_name",
        "middle_name",
        "is_active",
        "is_superuser",
    )
    search_fields = ("username",)
    list_filter = ("is_active", "is_superuser")
    inlines = [EquipmentUserTabularInline]

    def save_model(self, request, obj, form, change):
        """Хэширует пароль и сохраняет его в базе данных"""
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
