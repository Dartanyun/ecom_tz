from core.models import NameDescriptionModel
from django.db import models


class Category(NameDescriptionModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Stock(NameDescriptionModel):
    address = models.CharField(max_length=200, verbose_name="Адрес")

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Equipment(NameDescriptionModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, verbose_name="Склад"
    )
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество"
    )

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудования"
