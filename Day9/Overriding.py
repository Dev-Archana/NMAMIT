# class Employee:
#     def display(self):
#         print("Hello")
    
# # object
# e1=Employee() #Constructor 
# e2=Employee() #Constructor 
# e1.display()
# print(e1) 
# print(e2) 


# Create a student class and print the object reference 

# class Student:
#     def __init__(self,lname,fname):
#         self.lname=lname 
#         self.fname=fname
    
#     def __str__(self):
#         return self.lname+self.fname

#     def display(self):
#         print(self.lname)
#         print(self.fname)
# s1=Student("abc","xyz")
# del s1
# print(s1)
# s2=Student("abc123","xyz123")
# del To remove variable in a obejct 
# del s1.lname
# s1.display()

# s2.display()
# print(s1)

# print(s2)

class RandomNumber:
    x=10
    def display(self):
        global x
        x=8
        print(x)
    print(x)
s1=RandomNumber()
s1.display()

















