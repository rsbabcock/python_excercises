# Higher order function:
#     take another function as an arg
#     return a function

# Functions are first class citizen's in python

# def read_my_name(func):
#     name = "Fred"
#     name_thing = func(name)

#     return name_thing

# def make_a_phrase(name):
#     return f'Hi, my name is {name}'

# print(read_my_name(make_a_phrase))

def interior_decorator(func):
    def add_curtains(color):
        if color == "orange":
            color = "ugly-ass"
        func(color)
        print(f'now my house has {color} curtains')

    return add_curtains

# an example of functional programming
@interior_decorator
def move_in(color):
    print("my house was empty but . . .")

move_in("orange")
# bind returned function from interior_decorator to new variable - 
# new house is a reference to the function
# new_house = interior_decorator(move_in)
# new_house()    

# uncomment all above line by selecting all

# def add(num1, num2):
#     return num2 + num1

# def subtract(num1, num2):
#     return num1 - num2

# def calculator(func):
#     return func(3,4)

# result = calculator(add)
# print(result)    

# difference = calculator(subtract)
# print(difference)