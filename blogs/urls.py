from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = BlogsConfig.name


urlpatterns = [
    path("", BlogListView.as_view(), name="blog-list"),
    path("blog/<int:pk>", BlogDetailView.as_view(), name="blog"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="blog-update"),
    path("blog/<int:pk>/delete", BlogDeleteView.as_view(), name="blog-delete"),

]
