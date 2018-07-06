# This is a set
showroom = {'Mini Cooper', '67 Corvette Stingray', '67 VW Beetle', 'Tesla SUV'}
# This is the print method, kind of like a console log in js
print(len(showroom))
# this is the way to add to a set, extend and append don't work
showroom.add('Mini Cooper')
# print(showroom)

# using snake case added a new set
new_showroom = {'Ford Fiesta', 'Toyota Rav4'}
showroom.update(new_showroom)
# print(showroom)
# discard is like delete but in a set
showroom.discard('Ford Fiesta')
# print(showroom)

# new set
junkyard = {'Jeep Wrangler', 'Toyota Rav4', 'Ford Crown Vic', '93 Honda Civic', '67 VW Beetle'}
# union adds two sets together
showroom.union(junkyard)
# print(showroom.union(junkyard))
# intersection shows you where two sets have the same values
# print(showroom.intersection(junkyard))
showroom.discard('93 Honda Civic')
showroom.discard('Ford Crown Vic')

print(showroom)
