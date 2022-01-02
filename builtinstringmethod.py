#S.capitalize() : capitalize the 1st letter
#S.center(width, char): 
# S.count(sub, start, end): it will count how many substring appeared in string
#S.find(str,start,end): for findding
#S.index(str,start,end): same as find method according to index
#S.upper(): convert lower to upper
#S.lower(): convert upper to lover
#S.replace(old str, new str, count): count is otional
#S.split(dstr, count): count is optional
#S.swapcase()
#S.join(sequence)
#S.isalnum()
#S.isalpha()
#S.isdigit()
#S.islower()
#S.isspace()
#S.isnumeric()
#S.isdecimal()

S = "hello World"
print(S.capitalize())
print(S.find('t', 0, len(S)))
print(S.index('l', 0, len(S)))
print(S.lower())
print(S.upper())
print(S.center(15, '*'))
print(S.count('t', 0, len(S)))

print("\n")

print("examples from s.replace here:\n")

S1 = "Welcome to Python Programming"

print(S1.replace('o', '*', 2)) #replace twice as given arg is 2
print(S1.split(" "))
print(S1.swapcase())
print(S1.isalpha())
S1 = "Hello123"
print(S1.isdigit())
print(S1.isalnum())
print(S1.isalpha())
print(S1.lower())
S1 = "1236558"
print(S1.isdigit())
S1 ="hello"
print(S1.islower())