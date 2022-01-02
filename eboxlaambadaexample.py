exp = lambda x: x ** 3
print(exp(2)) 

print("\n")
myList = [lambda x: x ** 2,
 lambda x: x ** 3,
 lambda x: x ** 4]
 
for f in myList:
 print(f(3))

 print("\n")

 print((lambda e:e-2)(1))

 print("\n")
 o=lambda x=1,y=2,z=3:x+y+z
print(o(2) )

print("\n")

z=lambda a=2:print("Hello")
z() 

print("\n")
y=lambda :2+3
print(y())

print("\n")
numbers=[0,1,2,3,4,5,6,7,8,9,10]
a = list(filter(lambda x:x%3==0,numbers)) 
print(a)

print("\n")

numbers=[0,1,2,3,4,5,6,7,8,9,10]
b = list(map(lambda x:x%3==0,numbers))
print(b) 

print("\n")
z=lambda a=2:print("2Apple2")
print(z())

print("\n")

