class Parent:
    def __init__(self):
        print("Hello")
    
    # @staticmethod
    @classmethod
    def printing(cls):
        print("Hello")
    def Hi(self):
        print("Hi Method ")
p=Parent()
Parent.printing()
Parent.Hi()