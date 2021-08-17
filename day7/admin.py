from django.contrib.admin import ModelAdmin, register
from .models import Product, ProductCost, ProductCount, Customer, Order, OrderItem


@register(Product)
class ProductAdmin(ModelAdmin):
    pass


@register(ProductCount)
class ProductCountAdmin(ModelAdmin):
    pass


@register(ProductCost)
class ProductCostAdmin(ModelAdmin):
    pass


@register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    pass


@register(OrderItem)
class OrderItem(ModelAdmin):
    pass

