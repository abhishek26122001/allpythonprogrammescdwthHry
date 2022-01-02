# condition constructs are used when we want to execute the code having certain conditions are satisfied and knwon as decision 


# If Statement : It contains logical expression
# Finding tax for the user amount
tax = 0
num = input("Enter the Amount: \n")
if (float(num) > 50000):     # It was showing type error earlier as we didnt used float here to convert string format into numeric so we have to use float to reolve that error
    tax = (2 * float(num)) / float(100)
print("Total tax: ", tax)     

print("\n")

#If else satement 

print("If else statement example: Showing odd even number\n")

n = input("Enter the Number:  ")
if(float(n)%2==0):  # arguments converted of string into numbering using float
    print("It is even number")
else:
    print("it is odd")  

print("\n")

#if- elif statement examples

print("If - elif statement example: showing students grades\n")

S = input("Enter Your Marks:  ")
if(float(S)>=90):
    print("Grade: A+")
elif(float(S)<90 and float(S)>=75):
    print("Garde: A")    
elif(float(S)<75 and float(S)>=65):
    print("Garde: B")
elif(float(S)<65 and float(S)>=55):
    print("Grade: C")  
elif(float(S)<55 and float(S)>=40):
    print("Grade: D")
else:
    print("Garde: You are Failed")          