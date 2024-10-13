from dataclasses import dataclass

@dataclass
class Animal:
    all_animals = []
    def __init__(self,name,age):
        self._name = name
        self.age = age
        Animal.all_animals.append(self)
    def speak(self):
        print("my name is "+self.name)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def hello(message:str) -> str:
        print(message)
        return message



an = Animal('dog',12)
an.name = 'cat'
print(an.name)