import redis
from django.shortcuts import render, get_object_or_404
from .models import Product, Size
from django.conf import settings
from cart.forms import CartAddProductForm

def product_list(request):
    products = Product.objects.all()
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
    cart_product_form = CartAddProductForm()
    return render (
        request,
        'merch/product/detail.html',
        {'product': product, 'cart_product_form': cart_product_form}
    )





r = redis.Redis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    db = settings.REDIS_DB
)