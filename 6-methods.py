# 3 types of methods:
# 1.Instance method   2.static method   3.class method

# Types of Instance method:
# Type 1: The method which do not accept any parameter and doesnt have any return value.
# Type 2: The method which do not accept any parameter and has the return value. 
# Type 3: The method which accpets the parameter and does not have the return value. 
# Type 4: The method which accepts the parameter and has the return value. 


# Type 1: The method which do not accept any parameter and doesnt have any return value.
# class Calculator:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def add(self):
#         x=10
#         y=20
#         z=x+y
#         print("The sum is:",z)
# c1=Calculator()
# print(c1.a)
# print(c1.b)
# c1.add()



# Type 2: The method which do not accept any parameter and has the return value. 
# class Calculator:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def add(self):
#         x=10
#         y=20
#         z=x+y
#         return z
# c1=Calculator()
# print(c1.a)
# print(c1.b)
# res=c1.add()
# print(res)

# Type 3: The method which accpets the parameter and does not have the return value. 
# class Calculator:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def add(self,x,y):
#         z=x+y
#         print("the sum is:",z)

       
# c1=Calculator()
# print(c1.a)
# print(c1.b)
# a=15 
# b=20 
# c1.add(a,b)


# Type 4: The method which accepts the parameter and has the return value. 
class Calculator:
    def __init__(self):
        self.a=100
        self.b=200
    def add(self,x,y):
        z=x+y
        return z
c1=Calculator()
print(c1.a)
print(c1.b)
a=20 
b=30
res=c1.add(a,b)
print(res)



# Activation record is also called as stack frame - A block of memory is created in the stack when a function/method is called.
