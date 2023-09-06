"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

from src.item import Item, InstantiateCSVError

import pytest

import os


@pytest.fixture()
def test_file():
    emp1 = Item('iPhone', 100000, 5)
    return emp1


def test_calculate_total_price(test_file):
    assert test_file.calculate_total_price() == 500000


def test_apply_discount(test_file):
    Item.pay_rate = 0.5
    test_file.apply_discount()
    assert test_file.price == 50000


def test_name(test_file):
    assert test_file.name == 'iPhone'


def test_set_name(test_file):
    test_file.name = 'Pokemon'
    assert test_file.name == 'Pokemon'

    test_file.name = 'incomprehensibility'
    assert test_file.name == 'incomprehe'


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


# def test_instantiate_from_csv_file_not_found():
#     CSV_PATH = os.path.join(os.path.dirname(__file__), 'items2.csv')
#
#     # Вызов функции
#     with pytest.raises(FileNotFoundError):
#         Item.instantiate_from_csv(CSV_PATH)

# def test_instantiate_from_csv_file_corrupted():
#     # Подготовка данных
#     CSV_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')
#     file_content = [
#         {'name': 'item 1', 'price': '10.99', 'quantity': '5'}
#         {'name': 'item 2', 'price': '5.99', 'quantity': 'invalid'}
#
#     with open(CSV_PATH, 'w') as f:
#         writer = csv.DictWriter(f, fieldnames=['name', 'price', 'quantity'])
#     writer.writeheader()
#     writer.writerows(file_content)
#
#     # Вызов функции
#     with pytest.raises(InstantiateCSVError):
#         Item.instantiate_from_csv()


def test_string_to_number(test_file):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('6.9') == 6
    assert Item.string_to_number(553.654) == 553
    assert Item.string_to_number(92134.0) == 92134


def test_str(test_file):
    assert str(test_file) == 'iPhone'


def test_repr(test_file):
    assert repr(test_file) == "Item('iPhone', 100000, 5)"


def test_add():
    emp1 = Item('Laptop1', 1000400, 20)
    emp2 = Item('Laptop', 100000, 10)
    assert emp2 + emp1 == 30
    # assert emp1 + 1000 == None


def test_add_different_types():
    emp3 = Item('Laptop', 100000, 10)
    with pytest.raises(TypeError):
        emp3 + 10


def test_InstantiateCSVError():
    error = InstantiateCSVError()
    assert error.massage == 'Файл item.csv поврежден.'
