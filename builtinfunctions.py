#cmp(list1, list2):use to compare two functions and return reslt as 1 , -1 , or 0
#min(list): return the minimum function present in the list
#list(seq): convert any sequence into the list
#len(list): length of the list
#max(list): maximum function present in the list

from ast import Index
from typing import ChainMap


list1 = [10,12,13,18,20,59,62]
k = min(list1)
print(k)

print("-----------------------")

list1 = [25,85,196,25,87,69,85,23]
k = max(list1)
print(k)

print("-------------------------")

l = " Python "
k = list(l)
print(" ".join(k))
for i in k:
    print(i)



#list.append(obj): add object to end of the list
#list.count(obj): count the objects in the list
#list.extend(seq): append the contents of list
#list.index(obj): lowest index of the list
#list.insert(index,obj): insert the objects acc to index 
#list.pop(): remove last element from the list and return that element
#list.remove(obj): remove the object but do not return that obj\value
#list.remove(obj): it will remove the obj from list and change the original list
#list.reverse(): revesre the elements of the list from original list
#list.sort(): sort the element 
print("---------index---------------")
list2 = [12,10,15,11,14,13,12]
n = list2.index(10)
print(n)

print("---------append---------------")
list2 = [12,10,15,11,14,13,12]
n = list2.append(30)
print(list2)

print("----------append---------------")

l3 = [1,2]
list2.append(l3)
print(list2)
list2.extend(l3)
print(list2)

print("-----------insert-----------------")

list2 = [12,10,15,11,14,13,12]
list2.insert(2,25)
print(list2)

print("-----------reverse-----------------")

list2 = [12,10,15,11,14,13,12]
list2.reverse()
print(list2)

print("------------sort----------------")


list2 = [12,10,15,11,14,13,12]
list2.sort()
print(list2)

print("-----------Count------------------")
list2 = [10,15,48,15,56,95,15,85,25,75,15,85,15,64,15,85,15,85,45,15]
n = list2.count(15)
print(n)