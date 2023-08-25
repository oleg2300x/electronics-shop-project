"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_calculate_total_price():
    emp1 = Item('iPhone', 100000, 5)
    assert emp1.calculate_total_price() == 500000

def test_apply_discount():
    emp2 = Item('Watch', 10000, 2)
    Item.pay_rate = 0.5
    assert emp2.apply_discount() == 5000

