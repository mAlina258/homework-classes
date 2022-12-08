from BaseAnimal import *
from FoxAnimal import *

f = [FoxAnimal("Киллуа"), FoxAnimal("Гон")]

for i in f:
    i.DoSound()

for i in f:
    i.Eat(3, "мясо")

for i in f:
    i.IsFeeded()





