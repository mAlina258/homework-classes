from BaseAnimal import *

class RabbitAnimal(BaseAnimal):

    def __init__(self, name):
        super().__init__("Кролик", name)
        self.__age = 6
        self.__biome = "лес"
        self._sound = "фх-вш-фх"
        self.__liveSquare = 1  # размер клетки
        self.__mass = 1
        self.__isPredator = False  # хищник?
        self.__foodTypes = ["сено", "капуста"]  # продукты
        self.__foodVolume = 0.6  # кол-во еды
        self.__amountEaten = 0  # кол-во съеденного
        self.__isFeeded = False  # сытость


    def DoSound(self):
        print(self.name, "сказал/а на кроличьем: ", self._sound)


