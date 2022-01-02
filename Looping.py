#Types of Loops in Python
#  1. For Loop for sequence Structure: The for loop in python is used to iterate over a sequence(list, tuple, string) etc.

print("for loop in sequence struct.: ")

string = str(input("Enter the String\n")) #in order to make raw_input in python 3 we have to use fun(input(statement)) method
for i in string:
    print(i)

print("\n")

#For loop using Range Function

print("Range Function example: ")

n = int(input("Enter the End Value: \n"))
for i in range(0, n):
    print(i)

print("\n")

#For loop with Else

print("Pattern using for else loop:  ")

rows = 8
for i in range(0, rows):

    for j in range(0, i+1):

       print("*", end='')
    print("\n")       
else:
    print("Pattern Printed")    


