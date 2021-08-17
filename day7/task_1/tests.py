from day7.tests import (
    BaseTest,
)
from .implementation import (
    get_order_count_by_customer,
)


class ModelTest(BaseTest):

    def test_oleg(self):
        self.assertEqual(get_order_count_by_customer('Олег'), 2)

    def test_ivan(self):
        self.assertEqual(get_order_count_by_customer('Иван'), 3)

    def test_egor(self):
        self.assertEqual(get_order_count_by_customer('Егор'), 0)

    def test_fedot(self):
        self.assertEqual(get_order_count_by_customer('Федот'), 0)
