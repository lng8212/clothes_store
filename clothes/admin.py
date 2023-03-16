from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')
    
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'quantity')
    
class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(ProductOrder)