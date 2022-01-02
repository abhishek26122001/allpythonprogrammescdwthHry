# Having conditional Statements in another conditional Statements known as Nested Statements
#finding whether the number is positive - negative even or odd

num = input("Enter the Number:  ")
if(float(num) >= 0):
    if(float(num) % 2== 0):
        print("It is a Positive Even Number")
    else:
        print("It is a Positive Odd Number")
else:
    if(float(num) % 2== 0):
        print("Its is a Negative Even Number")
    else:
        print("It is A Negative Odd Number")               