from django.views.generic import ListView, DetailView, TemplateView

from blogs.models import BlogModel

class BlogListView(ListView):
    model = BlogModel
    template_name = 'blog.html'
    context_object_name = 'blogs'