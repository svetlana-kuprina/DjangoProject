
from django.db import models

from users.models import CustomUser


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    picture = models.ImageField(upload_to="photo/", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    publication = models.BooleanField(default=False, verbose_name="Публикация")
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="owner", verbose_name="Владелец", blank=True, null=True)


    def __str__(self):
        return f"Наименование {self.name} Цена {round(self.price)} Категория товара [{self.category}]"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "created_at", "updated_at", "price", "category"]
        permissions = [('can_unpublish_product', 'Can unpublish product')]
