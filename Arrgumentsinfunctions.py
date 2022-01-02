# Required, Keyword, Default, Variable length Arguments

#Required: Arguments passed to a function should be in correct Positional order
# Keyword: The caller identifies the arguments by paramter name
#Default: If we didnt appliied auny argument then it will take default value by its own
# variable length: We may need to process more function for more arguments than specified arguments in function defination

def fun(v1, *v2):
    print(v1)     
    for i in v2:
        print(i)
                                                     # Variable function
print("First Function")
fun(10)
print("Second Function")
fun(20, 30, 40, 50)

print("\n")


#Anonymous function: Because they are not defined as standard manner

square = lambda v: v*v

print("Square: ", square(2))
print("Square: ", square(20))


print("\n")

#Examples for Global and local

a = 0
def fun(c,d):
    a = c+d
    print("LOcal A: ", a)
fun(3,5)
print("GLobal A : ", a)    


print("\n")

v = 0
def fun(a, b):
    global v
    v = a+b
    print("Inside the function  v :  ", v)
print("Before Modification of v:  ", v)

fun(3,5)
print("Out Side the function v: ", v)