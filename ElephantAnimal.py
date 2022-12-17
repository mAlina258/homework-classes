from BaseAnimal import *

class ElephantAnimal(BaseAnimal):
    def __init__(self, name):
        super().__init__("Слон", name)
        self._age = 20
        self._biome = "саванна"
        self._sound = "*звуки слона*"
        self._liveSquare = 120  # размер клетки
        self._mass = 5000
        self._isPredator = False  # хищник?
        self._foodTypes = ["бананы", "сено"]  # продукты
        self._foodVolume = 50  # кол-во еды
        self._amountEaten = 0  # кол-во съеденного
        self._isFeeded = False  # сытость


    def DoSound(self):
        print(self.name, "сказал/а на слоновьем: ", self._sound)

