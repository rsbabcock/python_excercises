import unittest
from child import Child

class TestChild(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.sue = Child("sue")
    # Create an instance of the loot that can be used in all tests

    def test_item_delivered(self):
        self.sue.item_delivered()
        self.assertTrue(self.sue.item_delivered)

    def test_add_toy(self):
        sues_bike = self.sue.add_toy("bike")
        self.assertEqual(self.sue.add_toy("bike"), sues_bike)


if __name__ == '__main__':
    unittest.main()
