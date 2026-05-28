class Calculator:
    def add(self,a,b):
        res1=a+b
        return res1
    
    def sub(self,a,b):
        res2=a-b
        return res2
    
    def mult(self,a,b):
        res3=a*b
        return res3
    
    def div(self,a,b):
        res4=a/b
        return res4
    
c1=Calculator()
x=20 
y=10 
res1=c1.add(x,y)
res2=c1.sub(x,y)
res3=c1.mult(x,y)
res4=c1.div(x,y)
print("x + y =",res1)
print("x - y =",res2)
print("x * y =",res3)
print("x / y =",res4)