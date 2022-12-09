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

    def Eat(self, value, foodType):
        if (foodType in self.__foodTypes and value<= self.__foodVolume):
            self.__mass += value
            self.__amountEaten += value
            print("Лиса ", self.name, " говорит: покушал", value, foodType)
        else:
            print("Лиса ", self.name, " говорит: не буду", foodType)

    def IsFeeded(self):
        if (self.__amountEaten >= self.__foodVolume):
            self.__isFeeded = True
            print("Лиса ", self.name, " говорит: я наелся/ась!!")
        else:
            print(self.name, " говорит: я еще не наелся/ась")

    def Play(self):
        print("Лиса ", self.name, " говорит: поиграл!!")


