from .models import Product
from django.core.cache import cache

class ListProduct:

    @staticmethod
    def get_products_by_category(category):
        products = Product.objects.filter(category=category).order_by('id')
        return products

def get_products_cached():
    products = cache.get("product_list")

    if products is None:
        products = Product.objects.all()
        cache.set("product_list", products,  60 * 15)

    return products