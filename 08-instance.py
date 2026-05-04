# Declare a method in python and access instance variables within the method
class Student:
    def __init__(self):
        self.name="Manish"
        self.age=22 
        self.height=5.5
    def display(self):
        print(self.name)
        print(self.age)
        print(self.height)
s1=Student()
s1.display()
print(s1.name)
print(s1.age)
print(s1.height)
