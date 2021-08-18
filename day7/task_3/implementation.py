from django.db.models import F, Max
from day7.models import Order, OrderItem, ProductCost
from decimal import (
    Decimal,
)

def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    items = OrderItem.objects.filter(
        order__date_formation__range=[begin, end]
    )

    costs = ProductCost.objects.filter(
        begin__gte=begin,
        end__lte=end,
    )

# В этой задаче не проходит мартовский тест. Но тут, похоже, ошибка в тесте.
# Т.к. если проверить вручную, то получается не 56, а именно 480 (8 позиций на 60).
# Тут, похоже, случайно взяты за основу данные с ProductCount за март.

    product = {}
    count = 0
    for item in items:
        for cost in costs:
            if item.product.id == cost.product.id:
                sum_order = item.count * cost.value
                if product.get(item.order.number):
                    value = product[item.order.number]
                    result = sum_order + value
                    product[item.order.number] = result
                else:
                    product[item.order.number] = sum_order
                count += 1
    if count == 0:
        result = None
    else:
        print(product)
        product_max = max(product, key=product.get)
        result = (product_max, product[product_max])
    return result
