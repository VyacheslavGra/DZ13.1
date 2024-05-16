from src.item import Item


class Lang:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language.upper() != "EN" and language.upper() != "RU":
            raise ValueError("AttributeError: property 'language' of 'Keyboard' object has no setter")
        else:
            self.__language = language
    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"





class Keyboard(Item, Lang):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price,quantity)
        Lang.__init__(self)


kb = Keyboard('Dark Project KD87A', 9600, 5)
kb.language = 'EN'
kb.change_lang()
print(kb.language)
