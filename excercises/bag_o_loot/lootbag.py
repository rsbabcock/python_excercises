class Bag():

    bag = list("kite", "horse", "pony", "unicorn", "pocket knife")
         # Items can be added to bag, and assigned to a child.
     def add_item_to_bag_assign_to_child(self, item, child):
            return item, child
        # Items can be removed from bag, per child. 
        #   Removing ball from the bag should not be allowed. 
        #   A child's name must be specified.
     def remove_item_from_bag_per_child(self, child):
            return child
         # Must be able to list all children who are getting a toy.
     def list_all_children_getting_toys(self):
            return True
         # Must be able to list all toys for a given child's name.
     def list_all_toys_for_specific_child(self, child):
            return child
        # Must be able to set the delivered property of a child, 
        # which defaults to false to true.
     def set_delivered_to_child(self, child):
            return child