from django.db import (
    models,
)


class Product(models.Model):
    """
    Товар
    """
    name = models.CharField('Наименование', max_length=300)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class ProductCount(models.Model):
    """
    Количество товара
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    begin = models.DateField('Начало периода')
    end = models.DateField('Окончание периода')
    value = models.PositiveIntegerField('Значение')

    class Meta:
        db_table = 'product_count'

    def __str__(self):
        return f'{self.product.name} - {self.value}'


class ProductCost(models.Model):
    """
    Стоимость товара
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    begin = models.DateField('Начало периода')
    end = models.DateField('Окончание периода')
    value = models.DecimalField('Значение', max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'product_cost'

    def __str__(self):
        return f'{self.product.name} - {self.value}'


class Customer(models.Model):
    """
    Покупатель
    """
    name = models.CharField('Покупатель', max_length=300)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Заказ
    """
    number = models.CharField('Номер', max_length=50)
    date_formation = models.DateField('Дата')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Покупатель')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'Заказ № {self.number} ({self.customer.name})'


class OrderItem(models.Model):
    """
    Позиция заказа
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар')
    count = models.DecimalField(verbose_name='Количество', max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return f'Заказ: {self.product.name} в объеме {self.count}'