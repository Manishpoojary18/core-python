# local variable and instance variable
class Calculator:
    def __init__(self):
        self.a=10 #Instance variable
        self.b=20 #Instance variable
    def add(self):
        x=50 #local variable
        y=60 #local variable
        z=x+y #local variable
        print("The sum is:",z)
    def diff(self):
        num1=10 #local variable
        num2=5 #local variable
        num3=num1-num2 #local variable
        print("The diff is:",num3)
c1=Calculator()
print(c1.a)
print(c1.b)
c1.add()
c1.diff()

# local variables: variables declared inside a method/function. 
# instance variables: variables declared using self inside a class (inside __ini__)

