from src.Animal import Animal


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = "child name "+name
        self.age = age


    def speak(self):
        super().speak()
        print("from child class")
    
    def play(self):
        print("overloading")

    def play(self,play):
        print("overloading")