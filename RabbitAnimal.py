from BaseAnimal import *

class RabbitAnimal(BaseAnimal):
    def __init__(self, name):
        super().__init__("Кролик", name)
        self._age = 6
        self._biome = "лес"
        self._sound = "фх-вш-фх"
        self._liveSquare = 1  # размер клетки
        self._mass = 1
        self._isPredator = False  # хищник?
        self._foodTypes = ["сено", "капуста"]  # продукты
        self._foodVolume = 0.6  # кол-во еды
        self._amountEaten = 0  # кол-во съеденного
        self._isFeeded = False  # сытость


    def DoSound(self):
        print(self.name, "сказал/а на кроличьем: ", self._sound)


