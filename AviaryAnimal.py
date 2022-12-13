from BaseAnimal import *
class AviaryAnimal:

    def __init__(self, type):
        self.__type = type
        self.__square = 200
        self.__isPredator = False
        self.__biome = " "
        self.__animalInAviary = []

    def PopulateAnAnimal(self, animal:BaseAnimal):
        if (self.__biome == animal and self.__isPredator == False and self.__square >= self.__liveSquare):
            self.__animalInAviary.append(animal)

    def Feedind(self, food):
        if (self.__foodTypes = )
