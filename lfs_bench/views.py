# django imports
from django.http import HttpResponse

# lfs imports
from lfs.catalog.models import Product
from lfs.caching.utils import lfs_get_object_or_404

# ab -n1000 -c20 http://127.0.0.1/

def simple_response(request):
    """Delivers files to the browser.

    ~ 900 req/s
    """

    return HttpResponse("Hurz")

def simple_product(request):
    """Delivers files to the browser.

    With memcached: 500 req/s
    Without memcached: 120 req/s
    """
    product = lfs_get_object_or_404(Product, pk=1)
    return HttpResponse(product.name)
