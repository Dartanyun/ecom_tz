from django.db import models


class NameDescriptionModel(models.Model):
    """
    Абстрактная модель включающая в себя поля
    name, description. Модель необходима для поддержания DRY.
    """

    name = models.CharField(
        max_length=100, verbose_name="Название", unique=True
    )
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        abstract = True
        ordering = ("id",)

    def __str__(self):
        return self.name
