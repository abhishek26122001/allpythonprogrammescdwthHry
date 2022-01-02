#it is an unordered collection of items
# others have only value but dictionary has key:values pair as element
#defind with {} braces
# Keys should be unique, if keys are same then it will assign the value which is assigned lately or lastly
print("-----ACCESSING THE VALUE FROM DICTIONARY-----")

d = {"Name": "ABC", "AGE" : 26, "E-Mail": "abc231@gmail.com"}
print(d["Name"])
print(d["AGE"])
print(d["E-Mail"])
print("\n")

print("-----ITERATING THROUGH DICTIONARY------")

d ={ "NAME": "RAM SINGH", "ID": "190028", "E-MAil": "Ram2658@gmail.com"}
for i, j in d.items():
    print("Key: %s , Value: %s" %(i,j))

print("\n")

print("-----UPDATING VALUE FOR KEYS-----")

d = {"Name": "Shiinnu", "Age": 21}
d["Age"] = 19
print(d)
d["E-Mail"] = "Shinnu56@gmail.com"
print(d)

print("\n")

print("-----UDATATION OF EMPTY DICT.-----")

N = int(input("Enter no. of passes: "))
d ={}

for i in range(N):
    k = input("Enter Key: ")
    v = input("Enter Value: ")

    d[k] = v
print(d)    

print("\n")

print("-----USING RANGE FUNCTION IN DICTIONARY-----")

sqr = {X : X*X for X in range(8)}
print(sqr)

print("\n")

print("-----PROPERTIES OF DICT.-----")

d = {"NAME": "SHYAM", "AGE": 20}
del d["AGE"]
print(d)

d.clear()
print(d)