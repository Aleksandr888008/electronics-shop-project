from src.item import Item


# This Python file uses the following encoding: utf-8

class MixinLan:

    def __init__(self):
        super().__init__()
        self.language = None

    def change_lang(self):
        self.language = "RU"
        return self


class Keyboard(Item, MixinLan):

    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)

        self.language = language
