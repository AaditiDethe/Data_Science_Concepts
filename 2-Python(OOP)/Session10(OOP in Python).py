#############Object Oriented Programming in Python###############
'''Constructor--> don't return value
   class --> blueprint 
   object --> instance of class'''
class Human:
    def __init__(self,n,o): #constructor(explicit)
        self.name=n
        self.occupation=o
    
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots film")
            
    def speaks(self):
        print(self.name,"says how are you?")

tom=Human("tom_cruise","actor")  #tom is object
tom.do_work()
tom.speaks()

aaditi=Human("Aaditi","tennis player")
aaditi.do_work()
aaditi.speaks()

#################################################################
#Inheritance
'''Child class inherites the properties of Base class'''
class Vehicle():
    def general_usage(self):  #self --> is reference to the instance of class
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels=4
        self.has_roof=True
    
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")
        
class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheels=2
        self.has_roof=False
        
    def specific_usage(self):
        self.general_usage()
        self.wheels=2
        print("specific use: local communication, racing")
        
c=Car()
m=MotorCycle()
c.specific_usage()
m.specific_usage()
c.wheels
m.wheels
print(issubclass(Car,Vehicle))

#################################################################
class Father():
    def skills(self):  #this is not constructor
        print("I like gardening, programming")
    
class Mother():
    def skills(self): #this is not constructor
        print("I like cooking,art")
    
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)  #method of base class, calling by base class
        Mother.skills(self)
        print("I like sports")
        
c=Child()
c.skills()  #calling by the object of child class

#################################################################

    
