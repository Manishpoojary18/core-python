# Software
# software is collection of programs which is used to perform several tasks based on a business requirement
#Software is an automated solution for real-time problem



#Compilation is a process in which a compiler converts HLL into MLL during this process entire code is executing at one time
#Interpretation is  a process in which a interpreter converts HLL into MLL during this process single line of code is executin at one time


#Object- object is a physical entity
#Class- class is a blueprint of object

# steps for creating objects
# 1. The pvm allocates a new block of memory with new address in RAM
# 2. The pvm searches for one method (__inti__ method),once the method is found it allocating a memory for all the variables and assigns the Value
# 3. the address of the object should be given to the reference variable

class Student:
    def __init__(self):#self is used to store address of the object
        self.name="Manish"
        self.age=22
        self.addr="Bangalore"
        self.mob=767668
    def eat(self):
        print("Student is eating")
    def study(self):
        print("Student is studying")
s1=Student()
print(s1.name)
print(s1.age)
print(s1.addr)
print(s1.mob)
s1.eat()
s1.study()
s1.age=23
s1.addr="Udupi"
s2=s1
s3=s1
print(s2.name)
print(s3.age)
print(s1.addr)
print(s3.mob)