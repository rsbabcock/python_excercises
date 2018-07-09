from animal import Animal

class Python(Animal):

    def __init__(self, breed):
        self.breed = breed
        super().__init__("snake", leg_num=0, domesticated=True)
    

    def speak(self):
        return f' I am a python and I like to say {self.say_something()}'

