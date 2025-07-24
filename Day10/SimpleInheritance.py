# Simple Inheritance 
class Parent:
    def display(self):
        print('My Property Parent Class')
class Child(Parent):
    def display1(self):
        print("This is Child Class Property")
p=Child()
p.display()
p.display1()