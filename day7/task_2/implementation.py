from django.db.models import Count, Min
from day7.models import Customer


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    queryset = Customer.objects.filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).annotate(
        cnt=Count('order'),
        min_date=Min('order__date_formation')
    ).values(
        'cnt', 'name'
    ).order_by(
        '-cnt', 'min_date', 'name'
    ).first()

    if queryset:
        result = (queryset["name"], queryset["cnt"])
    else:
        result = None
    return result
