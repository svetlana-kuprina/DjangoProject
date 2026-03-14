from django.contrib import admin

from .models import BlogModel


@admin.register(BlogModel)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "number_of_views")
