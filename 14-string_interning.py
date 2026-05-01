#String interning: string interning is a process of storing a single copy of each unique string in "global intern pool" to achieve memory optimization. 
#Global intern pool stores a single copy of each umique string amd allows reuse to save memory. 
str1="Rama"
str2="Sita"
str3="Ravana"
str4="Rama"
str5="Rama"
str6="Sita"
str7="Ravana"
print(str1)
print(str2) 
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))
print(id(str6))
print(id(str7))