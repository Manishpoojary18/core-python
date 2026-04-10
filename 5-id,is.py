# id() function - It is a predefined function that returns the id of the provided vlaue.add()
# is operator - It checks whether both the values are in same memory location or not.
a=5
print(a)
print(id(a))

b=a
print(b)
print(id(b))
print(a is b)

c=a
print(c)
print(id(c))
print(a is c)


# Integer interning - It is a type of optimization technique used by python to resue small integer objects instead of creating new ones repeatedly.
# This saves memory and improves performance.
# By default, python interns integer from -5 to 256

d=20 
e=20 
f=20 
print(d)
print(e)
print(f)
print(id(d))
print(id(e))
print(id(f))
print(d is e)
print(d is a)
print(d is b)