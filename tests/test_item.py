import pytest

from src.item import Item


def test_calculate_total_price():
    item = Item('Смартфон', 20000, 100)
    assert item.calculate_total_price() == 2000000


def test_apply_discount():
    item = Item('Смартфон', 2000, 3)
    Item.pay_rate = 0.1

    item.apply_discount()

    assert item.price == 1800.0


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_truncate():
    item = Item('Телефон', 25000, 3)
    item.name = 'Суперсмартфон'
    assert item.name == 'Суперсмартфон'
