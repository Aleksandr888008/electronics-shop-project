import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.5
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def item_name(self):
        """
        Возвращает название товара.
        """
        return self.__name

    @item_name.setter
    def item_name(self, name):
        """
        Задает значение для названия товара, если оно не превышает 10 символов.
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("длина больше 10")


    @classmethod
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры класса Item данными из файла src/items.csv."""
        items = []
        with open('src/items.csv', encoding="windows-1251", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"]
                price = Item.string_to_number(row["price"])
                quantity = Item.string_to_number(row["quantity"])
                item = cls(name, price, quantity)
                items.append(item)
        return items

    @staticmethod
    def string_to_number(num):
        """Преобразует строку в число"""
        try:
            return int(num)
        except ValueError:
            raise ValueError("Не удалось преобразовать строку в число")

    def __repr__(self):
       """ Возвращает строковое представление экземпляра класса Item."""
       return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.quantity})'

    def __str__(self):
        """Возвращает строку с названием товара."""
        return f'{self.__name}'

