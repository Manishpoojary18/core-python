# Formal parameters: The variables which are declared during the method definition or while forming the methods is referred to as formal parameters
# Actual parameters/Arguments: The variables which are declared during the method call is referred to as actual parameters or arguments

class Demo:
    def swapcase(self,x,y):
        temp=x
        x=y
        y=temp
        return x,y
d1=Demo()
a=10
b=20 
print("Before swapping:")
print("a =",a)
print("b =",b)
a,b=d1.swapcase(a,b)
print("After swapping:")
print("a =",a)
print("b =",b)