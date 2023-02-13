from django.db import models

class Category(models.Model):
    name: models.CharField = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Advertisement(models.Model):
    name: str = models.CharField(max_length=200)
    author_id: str = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price: int = models.PositiveIntegerField()
    description: str = models.CharField(max_length=1000)
    is_published: bool = models.BooleanField()
    image = models.ImageField()
    category_id = models.ForeignKey("ads.Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
