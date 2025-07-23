class Employee:
    # name="archana"
    def __init__(self,name,age,salary):
        print(name)
        self.name=name
        print(age)
        print(salary)
        print(self.name)
        
    # String predefined method changed to user defined 
    # def __str__(self):
    #     return self.name+"Hello"
    
    # Method inside the class 
    def printing(self):
        print(f"{self.name}")
e1=Employee("Rani",25,200000)
print(e1)
# modifing the object
e1.name="raghu"
print(e1.name)
del e1.name
# print(e1.name)

del e1



# Inheritance In Python 
class Students:
    def __init__(self,fname,lname):
        self.lname=lname
        self.fname=fname
        
    def printDetails(self):
        print(f"{self.lname} {self.fname}")
class Marks(Students):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationYear=2025
        
s1=Students('LastName','FirstName')
s1.printDetails()
m1=Marks('lname','sname')
m1.printDetails()
print(m1.graduationYear)
# print(s1.graduationYear)    through an error because the properties present in super class can be accessed in subclass but we can do opposit of that
