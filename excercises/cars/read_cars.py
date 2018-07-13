# permission oprions: r: read only, w: write only, a: appending, r+: read and write
class Car():

    # def __init__(self):

    def read_car_makes(self):
        with open("car_makes.txt", "r") as makes_of_cars: 
        # print(type(list(makes_of_cars)))
            pretty_makes = list()
            for make in makes_of_cars:
                pretty_make = make[:len(make)-1]
                pretty_makes.append(pretty_make)
            return list(pretty_makes)  

    def read_car_models(self):
        with open("car_models.txt", "r") as models_of_cars:
            return list(models_of_cars)

    def get_dict_of_makes_and_models(self):
        # use above methods
        makes = self.read_car_makes()
        models = self.read_car_models()
        # iterate through return values
        # make dict out of values
        new_dict = dict()
        newer_dict = new_dict.fromkeys(makes)
        return print(new_dict.fromkeys(makes))
            # for make in makes:
            #     if make[0] in models:
                # key = make
                # value = models
car = Car()           
car.get_dict_of_makes_and_models()        

# with open("data/names.txt", "w") as names:
# def make_new_dict(make, model):
#   for name in nameset:
#     names.write(name + '\n')

# # later, back at the batcave...``
# with open("data/names.txt", "r") as names:
#   namelist = names.readlines()

# with open("data/nicknames.txt", "r") as nicks:
#   nicklist = nicks.readlines()

# mob_names = [f"{name.strip().split(' ')[0]} \"{nicklist[i].strip()}\" {name.strip().split(' ')[1]}" for i, name in enumerate(namelist)]

# print(mob_names)