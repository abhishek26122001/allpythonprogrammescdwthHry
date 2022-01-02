# Exmaple 1

def Odd(a, b):
    if a & 1 and b &1:
        print("Both are Odd")
    elif(a&1):
        print("%d is Odd"%(a))
    elif(b&1):
        print("%d is Odd"%(b))
Odd(3, 4)

print("\n")

# Example 2

def cube(x):
    return x * x * x      
x = cube(3)    
print(x)

print("\n")

# Example 3

def C2F(c):          
    return(c * 9//5 + 32) 
print(C2F(100)), 
print(C2F(0))

print("\n")

# Example 4

def power(x=1, y=2):
    r = 1
    for i in range(y):
        r = r * x
    return r

print(power())
print(power(3, 3))

print("\n")

# Example 5

x = 50
def func():
   global x
   print('x is', x),
   x = 2
   print('Changed global x to', x),
func()
print('Value of x is', x)

print("\n")

#Example 6

def a(b):        
    b = b.append(5)  
c = [1, 2, 3, 4] 
a(c) 
print(len(c))
