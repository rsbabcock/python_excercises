import unittest
from lootbag import Bag

class TestLootbag(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.loot = Bag()
    # Create an instance of the loot that can be used in all tests

    def test_add_item_to_bag_assign_to_child(self):
        sues_bag = self.loot.add_item_to_bag_assign_to_child("kite", "sue")
        self.assertEqual(self.loot.add_item_to_bag_assign_to_child("kite", "sue"), sues_bag)

    def test_remove_item_from_bag_per_child(self):
        self.assertEqual(self.loot.remove_item_from_bag_per_child("sue"), "sue")

    def test_list_all_children_getting_toys(self):
        self.assertTrue(self.loot.list_all_children_getting_toys)

    def test_list_all_toys_for_specific_child(self):
        self.assertEqual(self.loot.list_all_toys_for_specific_child("bebe"), "bebe")  

    def test_set_delivered_to_child(self):
        self.assertEqual(self.loot.set_delivered_to_child("joey"), "joey")

if __name__ == '__main__':
    unittest.main()
