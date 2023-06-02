from src.item import Item


# This Python file uses the following encoding: utf-8

class MixinLan:

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):

        if self.__language == "EN":
            self.__language = "RU"
            return self
        elif self.__language == "RU":
            self.__language = "EN"
            return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLan):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinLan.__init__(self)
