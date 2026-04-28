#String: string is a collection of characters or sequence of characters enclosed within quotes.  
#in python we can delcare the string in 4 ways:
# 'rama'
# "rama"
# '''rama'''
# """rama"""

str1="Rama"
print(str1) 
print(len(str1)) 
print(type(str1))

#strings are immutable, once we delcare the string we cannot able to modify anything within the same variable. 


#Indexing and Slicing in string

#Indexing: Accessing a single character from a string using its position 
str2="RajaRamMohanRoy"
print(len(str2))
print(str2[0])
print(str2[7])
print(str2[10])
print(str2[14])
print(str2[-1])
print(str2[-7])
print(str2[-11])
print(str2[-15])

#Slicing: Extracting a portion of a string using start, stop and step
str3="RajaRamMohanRoy"
print(str3[0:4])
print(str3[4:7])
print(str3[7:12])
print(str3[12:0]) #no output
print(str3[:])
print(str3[:7])
print(str3[7:])
print(str3[::-1]) #reverse
print(str3[6:0]) #no output     
print(str3[6:0:-1])
print(str3[-11:-8])
print(str3[-8:-3:-1]) #no output
print(str3[0:-11])
print(str3[-4:-9]) #no output
print(str3[-4:6:-1])
print(str3[:6:-1])
print(str3[6::-1])
print(str3[::2])
print(str3[0:7:0]) #error