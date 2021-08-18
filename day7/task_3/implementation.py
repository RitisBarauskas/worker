from django.db.models import F, Max
from day7.models import Order, OrderItem


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    queryset = OrderItem.objects.filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).annotate(
        max_order_sum=F('product__productcost__value') * F('count'),
        max_order_num=Max('order__number')
    ).values(
        'max_order_sum'
    ).order_by(
        '-max_order_sum',
        '-max_order_num'
    ).first()

    if queryset:
        result = queryset.get('max_order_sum')
    else:
        result = None

    return result
