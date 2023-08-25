
import csv

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name[:9]
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
        item_file = '../src/items.csv'
        with open(item_file, 'r') as w_file:
            file_reader = csv.DictReader(w_file)
            for row in file_reader:
                cls(row.get('name'), float(row.get('price')), int(row.get('quantity')))
    @staticmethod
    def string_to_number(num):
        return int(float(num))




