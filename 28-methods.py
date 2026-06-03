class Demo:
    def arith_op(self,x,y):
        add=x+y
        sub=x-y
        mult=x*y
        div=x/y
        return add,sub,mult,div

d1=Demo()
a=20 
b=10 
res1,res2,res3,res4=d1.arith_op(a,b) 
print("Add = {}\nSub = {}\nMult = {}\nDiv = {}".format(res1,res2,res3,res4))