family = {
    'sister': {
        'name': 'Arielle',
        'age': 26
    },
    'mother': {
        'name': 'Susan',
        'age': 59
    },
    'step-mother-in-law': {
        'name': 'Gina',
        'age': 46
    },
    'father': {
        'name': 'David',
        'age': 59
    },
    'brother': {
        'name': 'Michael',
        'age': 31
    },
    'husband': {
        'name': 'Daniel',
        'age': 33
    }
}

# classic for loop example
for x,y in family.items():
        print(f'my {x} is {y["name"]} and is {y["age"]} years old')

# uses comprehension method
my_family = {'my ' + k + ' is ' + v["name"] + ' and is ' + str(v["age"])  for (k,v) in family.items()}
print(my_family)

