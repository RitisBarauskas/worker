from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
from django.db.models import Count, Min
from .models import Product, ProductCost, ProductCount, Customer, Order, OrderItem
from .task_1.implementation import get_order_count_by_customer
from .task_2.implementation import get_top_customer_in_period


def index(request):
    return HttpResponse(get_top_customer_in_period(date(2021, 1, 1), date(2021, 1, 31)))
