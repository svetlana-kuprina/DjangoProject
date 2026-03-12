
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {"product": prod}
    return render(request, "product.html", context)


def contacts(request):
    return render(request, "contacts.html")
