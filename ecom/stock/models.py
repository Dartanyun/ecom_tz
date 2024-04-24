from core.models import NameDescriptionModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(NameDescriptionModel):
    class Meta:
        ordering = ("id",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Stock(NameDescriptionModel):
    address = models.CharField(max_length=200, verbose_name="Адрес")

    class Meta:
        ordering = ("id",)
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Equipment(NameDescriptionModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


class EquipmentUser(models.Model):
    """
    Связанная модель моделей Equipment и User.
    Модель необходима для M2M соотношения.
    """

    equipment = models.ForeignKey(
        Equipment,
        verbose_name="Оборудование",
        on_delete=models.CASCADE,
        related_name="users",
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="equipments",
    )
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество"
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Оборудование и пользователи"
        verbose_name_plural = "Оборудование и пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=["equipment", "user"], name="unique_equipment_user"
            )
        ]


class EquipmentStock(models.Model):
    """
    Связанная модель моделей Equipment и Stock.
    Модель необходима для M2M соотношения.
    """

    equipment = models.ForeignKey(
        Equipment,
        verbose_name="Оборудование",
        on_delete=models.CASCADE,
        related_name="stocks",
    )
    stock = models.ForeignKey(
        Stock,
        verbose_name="Склад",
        on_delete=models.CASCADE,
        related_name="equipments",
    )
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество"
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Оборудование и склады"
        verbose_name_plural = "Оборудование и склады"
        constraints = [
            models.UniqueConstraint(
                fields=["equipment", "stock"], name="unique_equipment_stock"
            )
        ]
