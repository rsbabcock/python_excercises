from dog import Dog
from pet import Pet
from python import Python
from animal import Animal
# or import dog to get the whole file

scout = Pet("Scout", Dog("Aussie"))
maya = Pet("Maya", Dog("Aussie"))
py = Pet("Py", Python("Monty"))

print(maya)

print(scout)

py.assign_owner('Steve')
print(py.__str__())