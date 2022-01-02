a={1:"A",2:"B",3:"C"}
b=a.copy()
b[2]="D"
print(a)

print("\n")
#Example 2

str1 = 'hello'
str2 = ','
str3 = 'world'
print(str1[-1:])

print("\n")
#Example 3

d={1:'a',2:'b',1:'A'}
print (d[1])

print("\n")

#example 4
l= [123, 'xyz', 'ABC', '456'];
print(l.pop(2))

print("\n")

#Example 5
a={'B':5,'A':9,'C':7}
print(sorted(a))

print("\n")

#example 7
print('xyyxyyxyxyxxy'.replace('xy', '12', 100)) 

print("\n")

#example 8
a={}
print(a.fromkeys([1,2,3],"check"))

print("\n")
#Example 9

Line1 = "And Then There Were None"
Line2 = "Famous In Love"
Line3 = "Famous Were The Kol And Klaus"
Line4 = Line1 + Line2 + Line3
print((Line1.find('Were'), Line4.count('And')))

print("\n")
#Example 10

a={"a":1,"b":2,"c":3}
b=dict(zip(a.values(),a.keys()))
print(b)

print("\n")

#example 11

count={}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
tot = 0
for i in count:
 tot=tot+count[i]
print(len(count)+tot) 