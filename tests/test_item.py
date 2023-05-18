import pytest

from src.item import Item

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

    # test_item.name = 'РучкаСинегоЦвета'
    # assert test_item.name == 'Больше 10 букв'
    # with pytest.raises(Exception):
    #     test_item.name = 'РучкаСинегоЦвета'


def test_repr(test_item):
    assert repr(test_item) == 'Item("Смартфон", 10, 20)'


def test_str(test_item):
    assert str(test_item) == "Смартфон"
