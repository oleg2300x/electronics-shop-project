"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

import pytest


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


def test_string_to_number(test_file):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('6.9') == 6
    assert Item.string_to_number(553.654) == 553
    assert Item.string_to_number(92134.0) == 92134
