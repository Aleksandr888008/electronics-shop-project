from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price():
    p1 = Item("Смартфон", 10, 20)
    assert Item.calculate_total_price(p1) == 200


def test_apply_discount():
    p2 = Item("Смартфон", 10, 20)
    p2.apply_discount()
    assert p2.price == 15.0


def test_item_name():
    p3 = Item('Бумага', 20, 30)
    assert p3.item_name == 'Бумага'

def test_item_name_s():
    item_name = 'Ручка'
    assert item_name == 'Ручка'

    # item_name = 'РучкаСинегоЦвета'
    # assert item_name == 'Больше 10 букв'
