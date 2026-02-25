from django.core.management import BaseCommand
from catalog.models import Product
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Add product to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        call_command('loaddata', 'product.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))