from django.db.models import Count, Min, Sum, F, Max
from day7.models import OrderItem


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    queryset = OrderItem.objects.values().filter(
        order__date_formation__gte=begin,
        order__date_formation__lte=end
    ).aggregate(Sum('count'))

    print(queryset)

    return queryset
