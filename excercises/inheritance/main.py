from dog import Dog
from pet import Pet
from animal import Animal
# or import dog to get the whole file

scout = Dog(breed="Aussie")
maya = Pet("Maya", Dog("Aussie"))

print(maya.__str__())

print(scout.speak())