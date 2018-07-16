class Child():

    def __init__(self, name):
        self.name = name
        self.toys = list()
        self.delivered = False

    def item_delivered(self):
        self.delivered = True
        return self.delivered

    def add_toy(self, toy):
        self.toys.append(toy)
        print(self.toys)
        return self.toys