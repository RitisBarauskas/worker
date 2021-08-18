from django.db.models import Count, Min, Sum, F, Max, Avg
from day7.models import OrderItem, ProductCost
from decimal import (
    Decimal,
)

def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    items = OrderItem.objects.filter(
        order__date_formation__range=[begin, end]
    ).exclude(product__name=product)
    product = {}
    count = 0
    for item in items:
        cost = ProductCost.objects.filter(
            begin__lte=item.order.date_formation,
            end__gte=item.order.date_formation,
            product__name=item.product.name
        ).first()
        if cost is None:
            continue
        sum_order = cost.value * item.count

        if product.get(item.order.number):
            value = product[item.order.number]
            result = sum_order + value
            product[item.order.number] = result
        else:
            count += 1
            product[item.order.number] = sum_order

    if count == 0:
        result = Decimal(0)
    else:
        result = sum(product.values()) / count

    return result
