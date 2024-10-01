class Animal:
    all_animals = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Animal.all_animals.append(self)
    def speak(self):
        print("my name is "+self.name)