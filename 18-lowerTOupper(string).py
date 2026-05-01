print("Enter a string:")
str1=input()
i=0
newstr=""
while(i<len(str1)):
    ext=str1[i]
    ascii=ord(ext)
    if (ascii>=90 and ascii<=122):
        newascii=ascii-32
        convchar=chr(newascii)
        newstr=newstr+convchar
    else:
        newstr=newstr+ext
    i+=1
print(newstr)