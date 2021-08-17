from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
from .models import Product, ProductCost, ProductCount, Customer, Order, OrderItem
from .task_1.implementation import get_order_count_by_customer


def index(request):
    return HttpResponse(get_top_customer_in_period(date(2021, 1, 1), date(2021, 1, 31)))


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    queryset = Order.objects.filter(date_formation__gte=begin, date_formation__lte=end)

    # dict_customers = {}
    # for order in queryset:
    #     customer_id = order.get('customer_id')
    #     if customer_id in dict_customers:
    #         dict_customers[customer_id] += 1
    #     else:
    #         dict_customers[customer_id] = 1
    # max_orders = max(dict_customers, key=dict_customers.get)
    # print(max_orders)
    return queryset
