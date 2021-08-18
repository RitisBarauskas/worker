from django.db.models import Count, Min, Sum, F, Max, Avg
from day7.models import OrderItem


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    queryset = OrderItem.objects.values().filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).annotate(
        order_sum=F('product__productcost__value') * F('count')
    ).exclude(
        product__name=product
    ).aggregate(
        Avg('order_sum')
    )

    if queryset:
        result = queryset.get('order_sum__avg')
    else:
        result = None

    return result
