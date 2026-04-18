from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from catalog.services import ListProduct, get_products_cached



class CatalogListView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"

    def get_queryset(self):
        return get_products_cached()


@method_decorator(cache_page(60 * 15), name='dispatch')
class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "product"


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        return super().form_valid(form)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner == self.request.user or self.request.user.has_perm("can_unpublish_product"):
            return obj
        else:
            raise PermissionDenied("У вас нет прав для удаления этого продукта.")


class TemplateContactView(TemplateView):
    template_name = "contacts.html"

class CatalogListProductView(DetailView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object.category
        context["products"] = ListProduct.get_products_by_category(obj)
        return context


