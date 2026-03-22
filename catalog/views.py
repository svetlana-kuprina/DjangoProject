from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class CatalogListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'


class CatalogDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class CatalogDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:home')





class TemplateContactView(TemplateView):
    template_name = 'contacts.html'
