#Finding a substring within the string
str1="If you think you can or you can't, you are right"
print(len(str1))
print(str1.find("you"))
print(str1.index("you"))
str2="you"
print(str2 in str1)
print(str1.rfind("you"))
print(str1.rindex("you"))
print(str1.find("rakesh"))  #-1
print(str1.index("rakesh")) #Error