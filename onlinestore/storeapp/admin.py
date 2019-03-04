from django.contrib import admin
from .models import ProductTypes, Products, Orders, Reviews
# Register your models here.

admin.site.register(ProductTypes)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Reviews)