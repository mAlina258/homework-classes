from BaseAnimal import *
from FoxAnimal import *
from ElephantAnimal import *
from RabbitAnimal import *

f = [FoxAnimal("Киллуа"), FoxAnimal("Гон")]
e = [ElephantAnimal("Нэмо"), ElephantAnimal("Дори")]

for i in f:
    i.DoSound()

for i in e:
    i.Play()

for i in e:
    i.Eat(3, "бананы")

for i in e:
    i.IsFeeded()

for i in f:
    i.IsFeeded()





