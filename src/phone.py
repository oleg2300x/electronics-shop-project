from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        if isinstance(number_of_sim, int) and number_of_sim >= 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __add__(self, other: int):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать экземпляр Phone или Item с экземпляром другого класса.")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
