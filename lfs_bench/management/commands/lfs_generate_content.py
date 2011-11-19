# django imports
from django.core.management.base import BaseCommand

# lfs imports
from lfs.catalog.models import Category
from lfs.catalog.models import Product

class Command(BaseCommand):
    args = ''
    help = 'Initializes LFS'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        
        for i in range(1, 10):
            category = Category.objects.create(nme="Name %s" % i, slug="slug %s" %s)
            for j in range(1, 10):
                Category.objects.create(nme="Name %s" % i, slug="slug %s" %s, parent=category)
                
        Product.objects.all().delete()
        for i in range(1, 100):
            Product.objects.create(name="Name %s" % i, slug="slug-%s" % i)
