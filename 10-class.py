# Standard way of writing the class

class Student:
    def __init__(self,name,age,height,addr):
        self.name=name
        self.age=age
        self.height=height
        self.addr=addr

s1=Student("Manish",22,5.5,"Bengaluru")
s2=Student("Vighnesh",22,5.5,"Mangalore")
print(s1.name,s1.age,s1.height,s1.addr)
print(s2.name,s2.age,s2.height,s2.addr)
