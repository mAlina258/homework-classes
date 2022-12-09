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

    def Eat(self, value, foodType):
        if (foodType in self.__foodTypes and value<= self.__foodVolume):
            self.__mass += value
            self.__amountEaten += value
            print("Кролик ", self.name, " говорит: покушал", value, foodType)
        else:
            print("Кролик ", self.name, " говорит: не буду", foodType)

    def IsFeeded(self):
        if (self.__amountEaten >= self.__foodVolume):
            self.__isFeeded = True
            print("Кролик ", self.name, " говорит: я наелся/ась!!")
        else:
            print(self.name, " говорит: я еще не наелся/ась")

    def Play(self):
        print("Кролик ", self.name, " говорит: поиграл!!")
