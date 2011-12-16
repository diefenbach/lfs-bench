# django imports
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args = ''
    help = 'Generates customers to benchmark LFS'

    def handle(self, *args, **options):
        from lfs.customer.models import Customer
        from lfs.customer.models import Address

        # Customer.objects.all().delete()
        try:
            amount = int(args[0])
        except:
            amount = 20

        for i in range(1, amount):
            customer = Customer.objects.create()

            address = Address.objects.create(
                firstname="Jane",
                lastname="Doe",
                customer=customer
            )

            customer.selected_invoice_address = address
            customer.save()
