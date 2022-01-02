class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last                                                # Single Inheritance
class Employee(Person):
    def __init__(self,staffnum, first, last):
        self.staffnumber = staffnum
        Person.__init__(self,first, last)
    def getEmployee(self):
        print("Employee Name: %s %s \nStaff Number: %d" %(self.firstname, self.lastname, self.staffnumber))

y = Employee(1007, "Raamlaal", "Dhinkar")
y.getEmployee()         #object


print("\n")

class Land_animal:
    def printing(self):                              # Multiple Inheritance
        print("This animal lives in land")
class Water_animal:
    def display(self):
        print("This animal lives in Water")
class frog(Land_animal, Water_animal):                       # Inherited class
    pass
f1 = frog()
f1.printing()                                         # Objects
f1.display()         

print("\n")


class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):                          # Multilevel Inheritance
        print("Barking")
class BabyDog(Dog):
    def weep(self):
        print("Weeping")
d = BabyDog()
d.eat()
d.bark()                      # Objects
d.weep()               



print("\n")

class Mammal:
    def __init__(self, mammalName):
        print(mammalName, "is a warm-blooded animal.")
class Dog(Mammal):                                                    # Super keyword in single inheritance
    def __init__(self, c):
        self.a = c
        print("Dog Has Four Legs.")
        super(Dog, self).__init__(self.a)
d1 = Dog("Dog")     



print("\n")


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, "is a cute Animal.")
class Dog:
    def display(self, petName):                                   # Super Key in Multiple inheritance
        print(petName, "is a warm - blooded Animal.")

class Cat(Mammal, Dog):
    def __init__(self, d):
        print("Cat is a Pet Animal.")
        super(Cat, self).__init__(d)        
        super(Cat, self).display(d)

d2 = Cat("Cat")        