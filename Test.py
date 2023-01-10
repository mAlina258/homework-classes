import unittest
from BaseAnimal import BaseAnimal
from FoxAnimal import FoxAnimal

class Test_Eat(unittest.TestCase):

    def setUp(self):
        self.foxAnimal = FoxAnimal("as")

    def test_IsFeeeded(self):
        self.foxAnimal:FoxAnimal
        self.foxAnimal.Eat("fsd", 423)
        actual = self.FoxAnimal.IsFeeded
        expected = False
        self.assertEqual(expected, actual)