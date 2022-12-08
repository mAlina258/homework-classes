class BaseAnimal:
    def __init__(self, type, name):
        self.__type = type
        self.name = name
        self.__age = 0
        self.__biome = " "
        self._sound = " "
        self.__liveSquare = 0      #размер клетки
        self.__mass = 0
        self.__isPredator = False    #хищник?
        self.__foodTypes = []      #продукты
        self.__foodVolume = 0        #кол-во еды
        self.__amountEaten = 0       #кол-во съеденного
        self.__isFeeded = False       #сытость

        @property
        def Types(self):
            return self.__type

        @property
        def Age(self):
            return self.__age

        @Age.setter
        def Age(self, value):
            if(value is int):
                if(value >=0):
                    self.__age = value

        @property
        def Sound(self):
            return self._sound

        @property
        def LiveSquare(self):
            return self.__liveSquare

        @property
        def Mass(self):
            return self.__mass

        @Age.setter
        def Mass(self, value):
            if (value is int):
                if (value >= 0):
                    self.__mass = value

        @property
        def IsPredator(self):
            return self.__isPredator

        @property
        def FoodTypes(self):
            return self.__foodTypes

        @property
        def IsFeeded(self):
            return self.__isFeeded

        def DoSound(self):
            print(self.name, "сказал/а: ", self._sound)

        def Eat(self, value, foodType):
            if (foodType in self.__foodTypes and value<= self.__foodVolume):
                self.__mass += value
                self.__amountEaten += value
                print(self.name, ": покушал", value, foodType)
            else:
                print(self.name, ": не буду", foodType)

        def IsFeeded(self):
            if (self.__amountEaten >= self.__foodVolume):
                self.__isFeeded = True
                print(self.name, " говорит: я наелся/ась!!")
            else:
                print(self.name, " говорит: я еще не наелся/ась")

        def Play(self):
            print(self.name, ": поиграл!!")


