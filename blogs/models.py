from django.db import models


class BlogModel(models.Model):

    name = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    preview = models.ImageField(upload_to="photo/", verbose_name="Превью", blank=True, null=True)
    publication_attribute = models.BooleanField(default=False, verbose_name="Опубликовать?")
    number_of_views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f" Заголовок: {self.name}, Количество просмотров: {self.number_of_views}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["name"]
