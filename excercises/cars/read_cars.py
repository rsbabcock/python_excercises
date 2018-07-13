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
            pretty_models = list()
            for model in models_of_cars:
                pretty_model = model[:len(model)-1]
                pretty_models.append(pretty_model)
            return list(pretty_models)  

    def get_dict_of_makes_and_models(self):
        # use above methods
        makes = self.read_car_makes()
        models = self.read_car_models()
        # iterate through return values
        # make dict out of values
        # newer_dict = new_dict.fromkeys(makes)
        # return print(newer_dict)

        # check if first letter of makes = first letter of model
        # if so add to newer dict
        # final_dict = {newer_dict[list()].append(l) for l in models if l[:1] == newer_dict.keys()}
        new_dict = dict()
        print(new_dict)
        for model in models:
            for make in makes:
                if model[:1] == make[:1]:
                    if make in new_dict:
                    # if make[:1] in new_dict:
                        new_dict[make].append(model[2:])                    
                    else:
                       new_dict[make] = [model[2:]]

        return(print(new_dict))

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