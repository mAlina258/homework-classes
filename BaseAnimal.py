class BaseAnimal:
    def __init__(self, type, name):
        self._type = type
        self.name = name
        self._age = 0
        self._biome = " "
        self._sound = " "
        self._liveSquare = 0      #размер клетки
        self._mass = 0
        self._isPredator = False    #хищник?
        self._foodTypes = []      #продукты
        self._foodVolume = 0        #кол-во еды
        self._amountEaten = 0       #кол-во съеденного
        self._isFeeded = False       #сытость

@property
def Predator(self):
    return self.__isPredator

@property
def Types(self):
    return self.__type

@property
def Age(self):
    return self.__age

@Age.setter
def Age(self, value):
    if(value is int and value >=0):
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
    if (value is int and value >= 0):
        self.__mass = value

@property
def IsPredator(self):
    return self.__isPredator

@property
def FoodTypes(self):
    return self.__foodTypes

@property
def IsFeeded(self):
    if (self.__amountEaten >= self.__foodVolume):
        self.__isFeeded = True
    return self.__isFeeded

def DoSound(self):
    print(self.name, "сказал/а: ", self._sound)

def Eat(self, value, foodType):
    if (foodType in self.__foodTypes and value<= self.__foodVolume):
        self.__mass += value
        self.__amountEaten += value
        print(self.__type, self.name, ": покушал", value, foodType)
    else:
        print(self.__type, self.name, ": не буду", foodType)

def Play(self):
    print(self.__type, self.name, ": поиграл!!")
