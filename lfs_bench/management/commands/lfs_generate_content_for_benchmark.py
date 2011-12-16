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
        Product.objects.all().delete()

        for i in range(1, 5):
            category = Category.objects.create(name="Name %s" % i, slug="slug-%s" %i)
            for j in range(1, 3):
                Category.objects.create(name="Name %s-%s" % (i, j), slug="slug-%s-%s" % (i, j), parent=category)

        c = Category.objects.get(slug="slug-1-1")
        for i in range(1, 20):
            p = Product.objects.create(name="Name %s" % i, slug="slug-1-%s" % i, active=True)
            p.categories.add(c)

        c = Category.objects.get(slug="slug-1-2")
        for i in range(1, 20):
            p = Product.objects.create(name="Name %s" % i, slug="slug-2-%s" % i, active=True)
            p.categories.add(c)

        from lfs.core.utils import set_category_levels
        set_category_levels()
