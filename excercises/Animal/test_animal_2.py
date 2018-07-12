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

  def test_animal_can_walk(self):
    self.bob.walk()
    print(self.bob.speed)
    self.assertEqual(self.bob.speed, 1.20)

  def test_animal_get_name(self):
    self.assertEqual(self.bob.get_name(), "Bob")   

  def test_animal_can_set_species(self):
    self.bob.set_species("Canine")  
    self.assertEqual(self.bob.species, "Canine")

  def test_animal_can_get_species(self):
    self.bob.set_species("Canine")
    self.assertEqual(self.bob.get_species(), "Canine")  

  def test_animal_gets_back_string(self):
    self.assertEqual(self.bob.__str__(), "Bob is a Canine")
    # self.assertEqual(self.bob.__str__(), sel)


if __name__ == '__main__':
      unittest.main()