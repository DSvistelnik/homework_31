from django.core.validators import MinLengthValidator
from django.db import models
from users.models import User

from validators import check_is_published

# Создание модели Категория

class Category(models.Model):
    name: models.CharField = models.CharField(max_length=200)
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)], unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    name: models.CharField = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    author: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    price: models.PositiveIntegerField = models.PositiveIntegerField()
    description: models.TextField = models.TextField(null=True, blank=True)
    is_published: models.BooleanField = models.BooleanField(validators=[check_is_published])
    image: models.ImageField = models.ImageField(upload_to="images/")
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Имя в единственном и множественном числе
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name

class Selection(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Advertisement)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
