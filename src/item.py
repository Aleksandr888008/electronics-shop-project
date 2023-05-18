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
        return self.__name

    @item_name.setter
    def item_name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise Exception("длина больше 10")
            # print('Больше 10 букв')

    @classmethod
    def instantiate_from_csv(cls):
        all = []
        with open('src/items.csv', encoding="windows-1251", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for r in reader:
                item = r['name'], r['price'], r['quantity']
                all.append(item)
                return cls(all)

    @staticmethod
    def string_to_number(num):
        return int(num)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'
