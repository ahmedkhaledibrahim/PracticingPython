# class variables = Shared among all instances of a class
# Defines outside the constructor
# allows you to share data among all objects

class Student:
    class_year = 2024
    num_students = []

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students.append(self)




s1 = Student("ahmed",23)
s2 = Student("khaled",23)

print(Student.class_year)
print(len(Student.num_students))