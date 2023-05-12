from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price():
    assert Item.calculate_total_price(10.0, 5) == 50.0


def test_apply_discount():
    assert Item.apply_discount(1, 1.5) == 1.5
