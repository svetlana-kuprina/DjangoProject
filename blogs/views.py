from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import BlogModel

class BlogListView(ListView):
    model = BlogModel
    template_name = 'blogs/blogs.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blogs/blog.html'
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    model = BlogModel
    template_name = 'blogs/blog_create.html'
    fields = ('name', 'content', 'preview', 'publication_attribute', 'number_of_views')
    success_url = reverse_lazy('blogs:blog-list')


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = 'blogs/blog_create.html'
    fields = ('name', 'content', 'preview', 'publication_attribute', 'number_of_views')
    success_url = reverse_lazy('blogs:blog-list')

class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blogs:blog-list')

