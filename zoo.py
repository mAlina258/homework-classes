class Fox:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.foodVolume = 5
        self.biome = "лес"
        self.square = 3
        self.__foodTypes = ["ягоды", "мясо"]
        self.predator = True
        self.sound = "фр-фр-фр"
        self.satiety = 0

    def DoSound(self):
        print(self.name, ":", self.sound)

    def Eat(self, foodType):
        if (foodType in self.__foodTypes):
            print(self.name, ": покушал", foodType)
        else:
            print(self.name, ": не буду", foodType)

    def Play(self):
        print(self.name, ": поиграл!!")



class Elephant:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.foodVolume = 50
        self.biome = "саванна"
        self.square = 120
        self.__foodTypes = ["бананы", "сено"]
        self.predator = False
        self.sound = "*звуки слона*"

    def DoSound(self):
        print(self.name, ":", self.sound)

    def Eat(self, foodType):
        if (foodType in self.__foodTypes):
            print(self.name, ": покушал", foodType)
        else:
            print(self.name, ": не буду", foodType)

    def Play(self):
        print(self.name, ": поиграл!!")

class Rabbit:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.foodVolume = 0.6
        self.biome = "лес"
        self.square = 1
        self.__foodTypes = ["сено", "капуста"]
        self.predator = False
        self.sound = "фх-вш-фх"

    def DoSound(self):
        print(self.name, ":", self.sound)

    def Eat(self, foodType):
        if (foodType in self.__foodTypes):
            print(self.name, ": покушал", foodType)
        else:
            print(self.name, ": не буду", foodType)

    def Play(self):
        print(self.name, ": поиграл!!")

