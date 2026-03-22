
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

class CatalogListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

class CatalogDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

class TemplateContactView(TemplateView):
    template_name = 'contacts.html'
