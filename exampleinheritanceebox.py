class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo's  __new__()  invoked")
    def __init__(self):
        print("Demo's  __init__()  invoked")
class Derived_Demo(Demo):
    def __new__(self):
        print("Derived_Demo's  __new__()  invoked")
    def __init__(self):
        print("Derived_Demo's  __init__()  invoked")
def main():
    obj1=Derived_Demo()
    obj2=Demo()
main()

print("\n")

#Example 2

class A:
    pass
class B(A):
    pass
obj=B()
print(isinstance(obj,A))

print("\n")

#Example 3

class  A:
    def  one(self):
        return  self.two()

    def  two(self):
        return  'A'

class  B(A):
    def  two(self):
        return  'B'
obj1=A()
obj2=B()
print(obj1.two(),obj2.two())

print("\n")

#example 4
class A(object):
    def __init__(self):
        self.__i = 1 
        self.j = 5 
    def display(self):
        print (self.__i, self.j)
class B(A):
    def __init__(self):
        super(B,self).__init__()
        self.__i = 2
        self.j = 7
c = B()
c.display()

print("\n")

#Example 5

class A():
    def disp(self):
        print("A disp()")
        
class B(A):
    pass


obj = B()
obj.disp()

print("\n")

# Example 6

class A:
    def __init__(self):
        self._x = 5
class B(A):
    def display(self):
        print(self._x)
def main():
    obj = B()
    obj.display()
main()

print("\n")

# Example 7

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1 
def main():
    obj = B()
    obj.count()
    print (obj.x, obj.y)
main()

print("\n")

# Example 8

class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

print("\n")

#example 


valid = False
while not valid:
    try:
        n=int(input("Enter a number"))
        while n%2==0:
            print("Bye")
            valid = True
    except ValueError:
        print("Invalid")

print("\n")

def f(x):
    yield x+1
    print("test")
    yield x+2
g=f(10)
print(next(g))
print(next(g))
