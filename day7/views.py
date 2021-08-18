from datetime import date
from django.http import HttpResponse
from decimal import (
    Decimal,
)
from .models import Product, ProductCost, ProductCount, Customer, Order, OrderItem
from .task_1.implementation import get_order_count_by_customer
from .task_2.implementation import get_top_customer_in_period
from .task_3.implementation import get_top_order_by_sum_in_period
from .task_4.implementation import get_top_product_by_total_count_in_period
from .task_5.implementation import get_average_cost_without_product


def index(request):
    return HttpResponse(get_average_cost_without_product('Молоко', date(2021, 1, 1), date(2021, 1, 31)))
