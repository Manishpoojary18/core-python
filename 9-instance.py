# Various ways to declare the instance variables:
#1.inside the class, inside the __init__ method.
#2.inside the class, inside the method.
#3.Outside the class.

#But the standard way to declare the instance variable is inside the class, inside the __init__ method(constructor).

class Heroine:
    def __init__(self):
        self.name="Radhika"
        self.age=40
        self.mob=789812
    def act(self):
        self.height=5.5
        self.addr="kodagu"

h1=Heroine()
# print(h1.name)
# print(h1.age)
# print(h1.mob)
h1.name="Ramya"
# print(h1.name)
h1.act()
h1.height=5.4
print(h1.name)
print(h1.age)
print(h1.mob)
print(h1.height)
print(h1.addr)