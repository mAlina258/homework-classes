from BaseAnimal import *
class BaseAviaryAnimal:

    def __init__(self, name):
        self._name = name
        self._square = 0
        self._remainingSpace = 0
        self._isPredator = False
        self._biome = " "
        self._animalInAviary = []
        self._foodInAviary = []


    # оставшееся место
    @property
    def RemainingSpace(self):
        if (self._remainingSpace > 0):
            return True
        else:
            return False

    @property
    def IsPredator(self):
        return self._isPredator

    @property
    def Biome(self):
        return self._biome

    def AnimalInAviary(self):
        return self._animalInAviary

    @property
    def Square(self):
        return self._square

    @Age.setter
    def Square(self, size):
        if (size is int and size <= 3 and size >=240):
            self._square = size

    def PopulateAnAnimal(self, animal:BaseAnimal):
        if (self._biome == BaseAnimal.biome and self._isPredator == BaseAnimal.isPredator and  self._remainingSpace >= self.BaseAnimal._liveSquare):
            self._animalInAviary.append(animal)
            self._remainingSpace -= BaseAnimal._liveSquare

    def RemoveTheAnimal(self, animal):
        self._animalInAviary.remove(animal)
        self._remainingSpace += BaseAnimal._liveSquare

    def FeedingAnimals(self, food, number):
        if (food == BaseAnimal._foodTypes):
            self._foodInAviary.append(food + number)

    def DoAnimalSound(self):
        for i in self._animalInAviary:
            BaseAnimal.DoSound()








