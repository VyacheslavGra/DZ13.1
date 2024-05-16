import csv
import os


class InstantiateCSVError(Exception):
    """
    Класс исключения при повреждении файла
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
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
        self.all.append(self)

    @property
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.quantity * self.price
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price - self.price * self.pay_rate

    @name.setter
    def name(self, value):
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        try:
            with (open("../src/items.csv", "rt", newline="", encoding="cp1251") as csv_file):

                reader = csv.DictReader(csv_file)

                for object in reader:
                    if "name" not in object or "price" not in object or "quantity" not in object:
                        raise InstantiateCSVError
                    cls(object["name"], object["price"], object["quantity"])
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        except InstantiateCSVError:
            print("InstantiateCSVError: Файл item.csv поврежден")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'
