
import csv
import os
CSV_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self.__name = name

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        # item_file = '../src/items.csv'
        with open(CSV_PATH, 'r') as w_file:
            file_reader = csv.DictReader(w_file)
            for row in file_reader:
                cls(row.get('name'), float(row.get('price')), int(row.get('quantity')))
    @staticmethod
    def string_to_number(num):
        return int(float(num))




