#multi line string using """
A = """Hello,,,                        
Welcome to Python Programming"""
print(A)
str = "This is a String" #single string
print(str)
print("Entered String is %s ! " %str) #value assigned to operator


#Accessing the characters by using slicing opt[] and substring using Range slicing[s:e]
#range will be done from s to e-1

# 0   1   2   3   4   5   6   7   8   9   10   11
# H   e   l   l   o       w   o   r   l   d    !
#-12 -11 -10 -9  -8   -7  -6  -5  -4  -3  -2  -1   Negative Indexing

S = 'Hello world!'
print("S[4] =" , S[4])
print("S[6:11] =" , S[6:11])
print("S[2:] =" , S[2:])
print("S[:4] =" , S[:4])
print("S[-1] =" , S[-1])
print("S[-8:-1] =" , S[-8:-1])
print("S[-2:] =" , S[-2:])
print("S[:-1] =" , S[:-1])

#Operator with string
# + sign use for concatenation 
# * sign is used for repetition 

s1 = "Python"
s2 = "Program"
print("New String 1 = ", s1 + s2)
print("New String 2 = " , s1 * 2)
print("New String 3 = ", s2 * 2)

s = s1[0:3] + 'P' + s1[4:] #String cant be modify we have to concatinate it to make changes as it is immutable
print(s)


