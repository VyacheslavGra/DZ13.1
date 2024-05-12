import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.setting import CSV, NOTFILE, CSVTEST


def test_init():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        item1 + 10


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv(CSV)
    assert len(Item.all) == 5


def test_instantiate_from_csv_test():
    assert Item.instantiate_from_csv_test(CSV) is True
    assert Item.instantiate_from_csv_test(NOTFILE) == 'Отсутствует файл items.csv'
    assert Item.instantiate_from_csv_test(CSVTEST) == 'Файл items.csv поврежден'


def test_name():
    item = Item('Смартфон', 10000, 5)
    item.name = "СуперСмартфон"
    assert len(item.name) <= 10
    assert item.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
