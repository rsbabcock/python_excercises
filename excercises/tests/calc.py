import unittest
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.calc = Calculator()
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  def test_subract(self):
    self.assertEqual(self.calc.subtract(5, 3), 2)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(5, 3), 15)

  def test_divide(self):
    self.assertEqual(self.calc.divide(10, 2), 5)
   
 
  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
