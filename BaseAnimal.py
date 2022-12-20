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
    return self._isPredator

@property
def Types(self):
    return self._type

@property
def Age(self):
    return self._age

@Age.setter
def Age(self, value):
    if(value is int and value >=0):
        self._age = value

@property
def Sound(self):
    return self._sound

@property
def LiveSquare(self):
    return self._liveSquare

@property
def Mass(self):
    return self._mass

@Age.setter
def Mass(self, value):
    if (value is int and value >= 0):
        self._mass = value

@property
def IsPredator(self):
    return self._isPredator

@property
def FoodTypes(self):
    return self._foodTypes

@property
def IsFeeded(self):
    if (self._amountEaten >= self._foodVolume):
        self._isFeeded = True
    return self._isFeeded

def DoSound(self):
    print(self.name, "сказал/а: ", self._sound)

def Eat(self, value, foodType):
    if (foodType in self._foodTypes and value<= self._foodVolume):
        self._mass += value
        self._amountEaten += value
        print(self._type, self.name, ": покушал", value, foodType)
    else:
        print(self._type, self.name, ": не буду", foodType)

def Play(self):
    print(self._type, self.name, ": поиграл!!")
