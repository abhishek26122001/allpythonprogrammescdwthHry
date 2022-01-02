# while loop example

i = 0
while i <= 10:
    print(i)
    i+= 1 #i++

print("\n")    

#while using else

c = 0
while c < 3:
    print(c)
    c = c + 1
else:
    print("Loop Ended")    

print("\n")


#Nested Loops: Loops inside loop

print("Nested loops examples: ")

# lets have pattern example using "Nested For loop"
for i in range(0, 4):
    for j in range(0, 4):
        print("*")
    print("\n")    


