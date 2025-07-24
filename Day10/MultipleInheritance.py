# Multiple inheritance : here we have more than one super type/class and one sub class
class Car:
    def printCarDetails(self):
        pass
class Bus:
    def printBusDetails(self):
        pass
class Vehicle(Car,Bus):
    pass