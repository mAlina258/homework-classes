from BaseAnimal import *
class FoxAnimal(BaseAnimal):
    def __init__(self, name):
        super().__init__("Лиса", name)
        self._age = 4
        self._biome = "лес"
        self._sound = "фр-фр-фр"
        self._liveSquare = 3  # размер клетки
        self._mass = 8
        self._isPredator = True  # хищник?
        self._foodTypes = ["ягоды", "мясо"]  # продукты
        self._foodVolume = 5  # кол-во еды
        self._amountEaten = 0  # кол-во съеденного
        self._isFeeded = False  # сытость

    def DoSound(self):
        print(self.name, "сказал/а на лисьем: ", self._sound)


