# Airthmetic operators (+, -, *, /, %)
print("Airthmetic Operartors: \n")

x = 15 
y = 4
print("x+y = ", x + y)
print("x-y = ", x - y)
print("x*y = ", x * y)
print("x/y = " , x / y)
print("x // y = ", x // y) # floor division
print("x**y =  ", x ** y) # x to power of y
print("x%y = " , x % y)

print("\n")


# Comparision Operators ( Flase and True )
print("Comparison operators: \n")

x1 = 10
y1 = 12
print("x1 > y1 = " , x1 > y1)
print("x1 < y1 = " , x1 < y1)
print("x1 == y1  = " , x1 == y1) # equal operator
print("x1  ! = y1 = " , x1 != y1) # not equal operator
print("x1 >= y1  is " , x1 >= y1) #greater then equal to
print(" x1 <= y1 is  ", x1 <= y1) # less then equal to

print("\n")

# Logical Operators ( and , or , not [true - false])
print("Logical Operators: \n")

a = True
b = False

print("a and b is " ,  a and b)
print(" a or b is " , a or b)
print(" not a is " , not a)
print(" not b is " , not b)

print("\n")


# Special Operators ( identity(is and is not) and membership(in and not in))
# is will work when memebers are identical or same and not is will work opposite to it
# in will work when members are in sequence and not in will work opposite to it
print("Special Opeartors: \n")

s1 = 5
t1 = 5
s2 = "Hello"
t2 = "Hello"            # identity Operators
s3 = [1,2]
t3 = [1,2]

print(s1 is not t1)
print(s2 is  t2)
print(s3 is  t3) # as it is muteable (list)



z = "Hello World"
w = {1 : 'a', 2 : 'b'}
print("H" in z)
print("hello" in z)     # Membership Function
print(1 in w)
print('a' in w)
print("Hello" not in  z)

print("\n")


# Bitwise Opearators
print("Bitwise Operator: \n")

c = 10
d = 5
print("C & d: ", c & d)
print("C | d: ", c | d)
print("~ c : ", ~ c)
print("C >> 1: ", c>>1)
print("d << 1: ", d<<1)

print("\n")

# Assingment Operator
print("Assingment Operator: \n")

r= 40
u = 21
r+=2 # r = r+2
u-=1 # u = u-1
r*=2 # r = r*2
print(r)
print(u)
