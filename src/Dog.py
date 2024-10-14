from src.Animal import Animal


class Dog(Animal):
    def speak(self):
        super().speak()
        print("speak from dog")

    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = "child name "+name
        self.age = age


    def play(self):
        print(f"{self.name} is playing")




d = Dog("doggy",5)
d1 = Dog("doggy2",5)
d2 = Dog("dogg3",5)
d3 = Dog("dogg4",5)
d4 = Dog("dogg5",5)

for animal in Animal.all_animals:
    print(animal.name)

d1.speak()