import pytest

from src.item import Item

from src.phone import Phone


phone1 = Phone('Samsung', 20000, 7, 2)
phone2 = Phone('iPhone', 80000, 10, 1)
phone3 = Item('Huawey', 7000, 7)
# phone4 = Phone('Oppo', 10100, 17, -2)


def test_init():
    assert phone1.number_of_sim == 2
    assert phone1.name == 'Samsung'
    assert phone1.price == 20000
    assert phone1.quantity == 7

# def test_phone_invalid_number_of_sim():
#     with pytest.raises(ValueError):
#         phone = Phone("Samsung", 599, 5, [2, 5, 6])

def test_add_different_types():
    with pytest.raises(TypeError):
        phone1 + 10


def test_repr():
    assert repr(phone1) == "Phone('Samsung', 20000, 7, 2)"

def test_add():
    assert phone1 + phone2 == 17
    assert phone1 + phone3 == 14
