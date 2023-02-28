from django.contrib.auth.models import AbstractUser
from django.db import models


# Создается модель Пользователей
class User(AbstractUser):
    ROLE: list[tuple] = [
        ("admin", "админ"),
        ("moderator", "модератор"),
        ("member", "участник"),
    ]
    role: models.CharField = models.CharField(max_length=50, choices=ROLE, default="member")
    age: models.PositiveSmallIntegerField = models.PositiveSmallIntegerField(null=True)
    locations: models.ManyToManyField = models.ManyToManyField("users.Location")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"

#Создание модели Локация

class Location(models.Model):
    name: models.CharField = models.CharField(max_length=250)
    lat: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    lng: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return f"{self.name}"
