# In order to solve the complex problems into smaller parts we devived them into several parts , these code of several parts are known as functions
#It is a block of organized , reusable code that is used to perform related actions.
# It avoid repetion and make code reusable,makes easier to understand, we can make them easier to debug, read and write

# Types: Built in functions and User Defined Functions : def function_functions(parameters):
#                                                        set of statements
#                                                        return[Expressio]

def fun(a):   #Defining Function
    print("Function has a value ", a)

print("Calling Function")
n = input()      
fun(n)           #fnction call


print("Passing Arguments\n")

def listAdd(mylist):
    mylist.append(8)
    print("Inside the Function: ", mylist)
    return

mylist = [1,5,7]
listAdd(mylist)    
print("Outside the Function: ", mylist)