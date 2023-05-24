from src.item import Item


# This Python file uses the following encoding: utf-8

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __repr__(self):
        """ Возвращает строковое представление экземпляра класса Phone."""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """Возвращает строку с названием товара."""
        return f'{self.__name}'
