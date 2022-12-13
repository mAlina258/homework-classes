from BaseAnimal import *

class FoxAnimal(BaseAnimal):

    def __init__(self, name):
        super().__init__("Лиса", name)
        self.__age = 4
        self.__biome = "лес"
        self._sound = "фр-фр-фр"
        self.__liveSquare = 3  # размер клетки
        self.__mass = 8
        self.__isPredator = True  # хищник?
        self.__foodTypes = ["ягоды", "мясо"]  # продукты
        self.__foodVolume = 5  # кол-во еды
        self.__amountEaten = 0  # кол-во съеденного
        self.__isFeeded = False  # сытость


    def DoSound(self):
        print(self.name, "сказал/а на лисьем: ", self._sound)


