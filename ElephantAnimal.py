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

    def Eat(self, value, foodType):
        if (foodType in self.__foodTypes and value<= self.__foodVolume):
            self.__mass += value
            self.__amountEaten += value
            print("Слон ", self.name, " говорит: покушал", value, foodType)
        else:
            print("Слон ", self.name, " говорит: не буду", foodType)

    def IsFeeded(self):
        if (self.__amountEaten >= self.__foodVolume):
            self.__isFeeded = True
            print("Слон ", self.name, " говорит: я наелся/ась!!")
        else:
            print(self.name, " говорит: я еще не наелся/ась")

    def Play(self):
        print("Слон ", self.name, " говорит: поиграл!!")
