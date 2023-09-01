from src.item import Item


class MixinLanguage:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self, language):
        return self.__language

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
            return self
        elif self.language == 'RU':
            self.__language = "EN"
            return self



class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int,):
        super().__init__(name, price, quantity)