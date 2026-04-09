from .models import Product

class ListProduct:

    @staticmethod
    def get_products_by_category(category):
        products = Product.objects.filter(category=category).order_by('id')
        return products