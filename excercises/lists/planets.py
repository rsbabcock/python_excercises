planet_list = ["Mercury", "Mars"]
# adds to the end
planet_list.append("Jupiter")
planet_list.append("Saturn")
# adds multiple list items
planet_list.extend(["Uranus", "Neptune"])
# adds to specific index value in list
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
# rocky_planets is a slice of rocky planets from planet list
rocky_planets = planet_list[0:4]
# delete syntax for getting rid of poor pluto
del planet_list[8]
# print(planet_list)
# print(rocky_planets)

# ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
sats = [('Victory', 'Saturn'), ('Apollo', 'Venus'), ('Cassini', 'Mars')]

def planets_with_sats():
    for planet in planet_list:
        for sat in sats:
            if sat[1] == planet:
                print(f'{sat[0]} is at {planet}')
                
planets_with_sats()                