
class Pet():

    # animal_type = Dog("aussie")
    #animal requires def __init__(self, species, leg_num=0, domesticated=False):
    def __init__(self, name, critter_instance):
        self.name = name
        self.animal_type = critter_instance
        # super().__init__("dog", leg_num=4, domesticated=True)

    def assign_owner(self, owner):
        self.owner = owner

    def __str__(self):
        return f'this pets name is {self.name}. It has {self.animal_type.leg_num} legs and likes to say {self.animal_type.say_something()}'

# 1) Give a pet its own prop of name
# 2) Give it a property of animal_type
# 3) animal_type needs to be an instance of a dog
# 4) assign an owner via a method
# 5) __str__ return a string with pet's name, # of legs, and what it says    # 
