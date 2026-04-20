# Static variable:
#The variable which is declared inside the class but outside the __init__ method and all the other methods is referred to asStatic variable. 
#for the static variable, it will allocate memory only once irrespective of the number o objects created. 

class Demo:
    x=99
    y=88
    def __init__(self):
        self.a=10
        self.b=20

d1=Demo()
d2=Demo()
d3=Demo()
print(Demo.x)
print(Demo.y)
Demo.x=199
Demo.y=188
print(Demo.x)
print(Demo.y)
print(d1.a)
print(d2.b)