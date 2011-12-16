# django imports
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args = ''
    help = 'Generates customers to benchmark LFS'

    def handle(self, *args, **options):
        from reviews.models import Review
        from lfs.catalog.models import Product

        p = Product.objects.all()[1]

        Review.objects.all().delete()
        try:
            amount = int(args[0])
        except:
            amount = 20

        for i in range(1, amount):
            review = Review.objects.create(content=p)
