from django.contrib import admin
from .models import Product, Size

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image','description','price','sizes']

# @admin.register(Size)
# class SizeAdmin(admin.ModelAdmin):
#     list_display = []
# Not sure if needs to be registered