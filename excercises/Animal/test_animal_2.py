import unittest
import sys
sys.path.append('../')
from animal_2 import Animal
from animal_2 import Dog


class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.bob = Dog("Bob")
    # Create an instance of the calculator that can be used in all tests

  def test_animal_creation(self):

    bob = Dog("Bob")

    self.assertIsInstance(bob, Dog)
    self.assertIsInstance(bob, Animal)

  def test_animal_can_set_legs(self):
    self.bob.set_legs(6)
    self.assertEqual(self.bob.legs, 6)

if __name__ == '__main__':
      unittest.main()