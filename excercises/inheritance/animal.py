class Animal():
    
  def __init__(self, species, leg_num=0, domesticated=False):
    self.species = species
    self.leg_num = leg_num
    self.domesticated = domesticated

  def say_something(self):
    print(self.species )
    if self.species == "dog":
      return "woof"
    else:
      return "moosqueakrrrrrchirp"