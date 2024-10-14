from typing import Protocol


class Animal:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"my name is {self.name}, I make {self.sound} sound")



class Prey(Protocol):
    def flee(self):
        pass


class Rabbit(Animal):
    def __init__(self,name,age,sound,color):
        super().__init__(name,age,sound)
        self.color = color

    def speak(self):
        super().speak()
        print("I'm Rabbit")

    def flee(self):
        pass


r1 = Rabbit("loony",1,"sdfs","white")
isPrey = r1 is Prey
print(isPrey)


