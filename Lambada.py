
def Sum3(a ,b, c):
    d = a + b + c
    return d
                              # This is the simple function example using def and all
a, b, c = map(int, input("Enter three Numbers in one row: "). split(" "))
print("Output Using def function: ",Sum3(a, b, c))


print("\n")

# This is the example using lambada function

sum3 = lambda a, b, c:a+b+c
a, b, c = map(int, input("Enter three Numbers in one row: "). split(" "))
print("Output using Lambda function: ",Sum3(a, b, c))


print("Maximum Number Finder\n")

def max2(a, b):
    if a>b:
        return a
    else:                                        # Maximum between two Numbers using def function
        return b   

a, b = map(int, input("Enter two Numbers in one row: "). split(" "))
print("Output using def function: ",max2(a, b))


print("\n")

max2 = lambda a, b: a if a>b else b                                      # Maximum between two Numbers using lambda function

a, b = map(int, input("Enter two Numbers in one row: "). split(" "))
print("Output using lambda function: ",max2(a, b))


print("\n")

max3 = lambda a, b, c: a if a>b and a>c else b if b>c else c                    # Maximum between three Numbers using lambda function

a, b, c = map(int, input("Enter three Numbers in one row: "). split(" "))
print("Output using lambda function: ",max3(a, b, c))



print("Print the square using map function of number\n")

sq = lambda a: a*a

l = [2, 3, 4, 5, 6, 7]
sql = list(map(sq, l))                # Map Function
print(l)                                            
print(sql)


print("Filter function example\n")

even = lambda a: a%2==0

l = [2, 3, 4, 5, 6, 7, 8, 10, 12]
evl = list(filter(even, l))                        # Filter function
print(l)
print(evl)




print("\n")

print("Reduce function example: ")

from functools import reduce

con = lambda a,b : a+b                                           # Reduce function
l =["A", "B", "H", "I", "S", "H", "E", "K"]
s = reduce(con, l)

print(l)
print(s)
