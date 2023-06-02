# This Python file uses the following encoding: utf-8
import pytest

from src.keyboard import Keyboard, MixinLan


@pytest.fixture
def test_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(test_keyboard):
    assert str(test_keyboard) == "Dark Project KD87A"


def test_language(test_keyboard):
    assert str(test_keyboard.language) == "EN"


def test_change_lang(test_keyboard):
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == "RU"


def test_change_lang_two(test_keyboard):
    test_keyboard.change_lang().change_lang()
    assert str(test_keyboard.language) == "EN"
