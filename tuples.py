# it is similar to list but it is immutable datatype in Python
#They are used to store write-product data as it is imutable so no changes can be done in the data
#a = () or tuple()
# As it is immutable but we can use contents existing for creating new tuple(concatination)

print("Tuple Example: ")

T =(5,1,2,9.7)
print(T[0])
print(T[-1])
print(T[: 1])
print(T[1:4])

t1 = (5,1,2,9.7)
t2 = (3, "Hello")
R = t1+t2
print(R)

print("\n")

N = int(input())
T = ()

for i in range(N):
    v = input()
    T = T + (v,)
print(T)

print("---------------Basic Functions of tuples----------------")

L = (5,1,2,9.7)
print(L +("ABC", 0))
print(L*3)
print(len(L))
print(min(L))
print(max(L))
print(tuple("Hello"))

