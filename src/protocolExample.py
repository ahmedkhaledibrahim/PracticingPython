from typing import Protocol

class Flyer(Protocol):
    def fly(self):
        print("I can Fly")


class Bird:
    def fly(self):
        print("bird can fly")

class Plane:
    def fly(self):
        print("plane can fly")

def who_can_fly(ob:Flyer):
    ob.fly()

who_can_fly(Plane())