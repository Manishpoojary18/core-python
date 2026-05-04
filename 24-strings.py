#Removing the spaces inbetween the string
print("Enter a string:")
str=input()
i=0 
nstr=""
while(i<=len(str)-1):
    data=str[i]
    if (data==" "):
        i+=1
    else:
        nstr=nstr+data
        i+=1
print(nstr)


#Using inbuild method
str1="R a m a"
str2=str1.replace(" ","")
print(str2)