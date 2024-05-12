import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        self.__name = name_
        if len(self.__name) > 10:
            self.__name = self.__name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Преобразует файл csv  в словарь.
        """
        if Item.instantiate_from_csv_test(path) is True:
            Item.all = []
            with open(path, 'r', encoding="utf-8") as csvfile:
                reader: csv.DictReader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def instantiate_from_csv_test(path):
        """
        Проверка наличия и целостности файла
        """
        try:
            with open(path, 'r', encoding="utf-8") as csvfile:
                reader: csv.DictReader = csv.DictReader(csvfile)
                reader_dict = list(reader)
                for i in reader_dict:
                    if (i.get('name') and i.get('price') and i.get('quantity')) in ['', None]:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print('Отсутствует файл items.csv')
            return 'Отсутствует файл items.csv'
        except InstantiateCSVError as ex:
            print(ex.message)
            return ex.message
        else:
            return True


class InstantiateCSVError(Exception):
    """
    Исключение при пофрежденном файле
    """
    def __init__(self):
        self.message = 'Файл items.csv поврежден'
