import unittest
from lootbag import Bag

class TestLootbag(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.test_loot = Bag()
    # Create an instance of the calculator that can be used in all tests

  def test_add_item_to_bag_assign_to_child(self):
    self.assertTrue(self.test_loot)
 
  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
