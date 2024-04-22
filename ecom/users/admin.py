from django.contrib import admin
from django.contrib.auth.hashers import make_password
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админ панель модели пользователей.
    """

    list_display = ("username", "is_active", "is_superuser")
    search_fields = ("username",)

    def save_model(self, request, obj, form, change):
        """Хэширует пароль и сохраняет его в базе данных"""
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
