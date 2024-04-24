from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from users.manager import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Кастомная таблица пользователей"""

    USERNAME_FIELD = "username"

    username = models.CharField(
        max_length=100, blank=False, verbose_name="Логин", unique=True
    )
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    middle_name = models.CharField(
        verbose_name="Отчество", max_length=150, blank=True
    )
    password = models.CharField(
        verbose_name="Пароль",
        blank=False,
        max_length=200,
    )
    is_staff = models.BooleanField(
        "Стафф статус",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="Админ статус",
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name="Активный пользователь", default=False
    )

    objects = MyUserManager()

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
