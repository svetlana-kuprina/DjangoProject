from django.core.management import BaseCommand
from catalog.models import Category
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Add category to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        call_command('loaddata', 'category.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))