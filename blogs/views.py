from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import BlogModel


class BlogListView(ListView):
    model = BlogModel
    template_name = "blogs/blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = "blogs/blog.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = BlogModel
    template_name = "blogs/blog_create.html"
    fields = ("name", "content", "preview", "publication_attribute", "number_of_views")
    success_url = reverse_lazy("blogs:blog-list")


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = "blogs/blog_create.html"
    fields = ("name", "content", "preview", "publication_attribute", "number_of_views")
    success_url = reverse_lazy("blogs:blog-list")

    def get_success_url(self):
        return reverse("blogs:blog", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = "blogs/blog_delete.html"
    success_url = reverse_lazy("blogs:blog-list")
