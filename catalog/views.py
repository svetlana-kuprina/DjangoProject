from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "base.html", {"products": products})


def contacts(request):
    return render(request, "contacts.html")
