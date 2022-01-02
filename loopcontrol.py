#Break Statement

print("Break Statement: ")

while(True):
    n = input()
    if(int(n) ==0):
        break           # it terminates the whole loop
    else:
        print(n) 


print("\n")

# continoue Statement

print("Continoue Statement: ")

N = input("Enter number to check even numbers: ")
for i in range(0, int(N)+1):
    if(int(i) % 2 == 1):
        continue   # terminates the particular loop that is specified
    print(i)

print("\n")

# Pass Statement

print("Pass Statement: ")    

Str = "Hello"
for val in Str: 
    pass  # it is a null statement, nothing will executed during this, it is as a placeholder, used in abstract classes
# because in abstract classes we have to leave the body of function defination

