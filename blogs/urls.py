from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView


app_name = BlogsConfig.name


urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="blog-list"),
]
