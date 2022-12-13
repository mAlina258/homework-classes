from BaseAnimal import *

class ElephantAnimal(BaseAnimal):

    def __init__(self, name):
        super().__init__("Слон", name)
        self.__age = 20
        self.__biome = "саванна"
        self._sound = "*звуки слона*"
        self.__liveSquare = 120  # размер клетки
        self.__mass = 5000
        self.__isPredator = False  # хищник?
        self.__foodTypes = ["бананы", "сено"]  # продукты
        self.__foodVolume = 50  # кол-во еды
        self.__amountEaten = 0  # кол-во съеденного
        self.__isFeeded = False  # сытость


    def DoSound(self):
        print(self.name, "сказал/а на слоновьем: ", self._sound)

