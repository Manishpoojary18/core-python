class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def class_method(cls,s_info):
        name,age=s_info.split()
        return cls(name,int(age))
    
s1=Student.class_method("Manish 22")
print(s1.name) 
print(s1.age)   