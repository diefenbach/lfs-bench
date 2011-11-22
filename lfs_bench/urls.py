# django imports
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('lfs_bench.views',
    url(r'^simple-response$', "simple_response"),
    url(r'^simple-product$', "simple_product"),
)
