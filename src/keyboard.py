from src.item import Item


# This Python file uses the following encoding: utf-8

class MixinLan:

    def __init__(self):
        super().__init__()
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self
        elif self.language == "RU":
            self.language = "EN"
            return self
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    @property
    def keyboard_language(self):
        return self.language


class Keyboard(Item, MixinLan):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

        MixinLan.__init__(self)

        # self.language = language

    # @property
    # def keyboard_language(self):
    #
    #     return self.__language
