import redis
from django.shortcuts import render, get_object_or_404
from .models import Product, Size
from django.conf import settings

def product_list(request):
    products = Product.published.all()
    return render (
        request,
        'merch/product/list.html',
        {'products': products}
    )

def product_detail(request, product):
    product = get_object_or_404(
        Product,
        slug = product
    )
    return render (
        request,
        'merch/product/detail.html',
        {'product': product}
    )





r = redis.Redis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    db = settings.REDIS_DB
)