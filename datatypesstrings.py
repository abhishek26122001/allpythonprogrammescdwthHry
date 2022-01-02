#string is sequence of characters
#strings are immutable in Python : we can't replace them and there is no charachtertype
A = """Hello,,,,,,,
Welcome to Python Programming"""
print(A)

str = "This is a String"
print(str)
print("Entered String is %s !" %str)

print("\n")

#String Built In Functions
# len(x) : it will return the length of corrosponding string
#max(x) : it will return the maximum alphabetical char in string as ASCII value range
#min(x): it will return the minimum alphabetical char in string as ASCII Value Range
#str(x): it will convert corrosponding object into string obj
#ord(x) : it will return the ASCII vslue of any char value
#chr(x) : it will be opposite to ord(x)
#unichr(x) : it will same as the chr(x) but return the unicode
#repr(x) : convert corrosponding x into expression
#complex(r,i): complex numbers

print("Examples on String Built In fnc\n")

S = "Python"
print(len(S))
print(max(S))
print(min(S))
print(ord('A'))
print(chr(97))
print(repr(123))
print("%s" %complex(2,4))
