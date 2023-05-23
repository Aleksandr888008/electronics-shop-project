# This Python file uses the following encoding: utf-8

from src.phone import Phone
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля Phone."""


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 13", 120_000, 10, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + phone2 == 15
    # assert phone1 + 10 == 15  #ValueError('Складывать можно только объекты Item и дочерние от них.')
    try:
        not isinstance(Phone, Item)
    except ValueError as e:
        assert e == 'Складывать можно только объекты Item и дочерние от них.'
