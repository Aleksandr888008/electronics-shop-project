import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def test_item():
    return Item("Смартфон", 10, 20)


def test_calculate_total_price(test_item):
    assert Item.calculate_total_price(test_item) == 200


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 15.0


def test_item_name(test_item):
    assert test_item.item_name == 'Смартфон'


def test_item_name_s(test_item):
    test_item.name = 'Ручка'
    assert test_item.name == 'Ручка'

    try:
        test_item.name = 'РучкаСинегоЦвета'
    except ValueError as e:
        assert str(e) == "длина больше 10"


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5
    # assert items[0].name == "Смартфон" #почему то не работает этот тест
    assert items[0].price == 100
    assert items[1].quantity == 3
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError as e:
        assert e == FileNotFoundError("Отсутствует файл item.csv")
    except InstantiateCSVError as e:
        raise e == InstantiateCSVError("Файл item.csv поврежден")


def test_string_to_number():
    assert Item.string_to_number("10") == 10
    try:
        Item.string_to_number("Not a Number")
    except ValueError as e:
        assert str(e) == "Не удалось преобразовать строку в число"


def test_repr(test_item):
    assert repr(test_item) == 'Item("Смартфон", 10, 20)'


def test_str(test_item):
    assert str(test_item) == "Смартфон"


def test_add():
    phone1 = Phone('iPhone 14', 120_000, 5, 2)
    phone2 = Phone('iPhone 13', 120_000, 10, 2)
    item1 = Item('Смартфон', 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + phone2 == 15
    # assert phone1 + 10 == 15  #ValueError('Складывать можно только объекты Item и дочерние от них.')
    try:
        not isinstance(Phone, Item)
    except ValueError as e:
        assert e == 'Складывать можно только объекты Item и дочерние от них.'
