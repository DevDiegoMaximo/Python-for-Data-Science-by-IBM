#Tuples and Lists

TupleTest = (1, "str", 2.2)

#Nesting example

Nesting = (3, 1, ("str", 3), (5,6), ("disco", (1,2)))

print(Nesting[2])
print(Nesting[2][1])

#Lists
#Lists are MUTABLE, this is the MAIN difference between tuples and lists

L=["MJ", 10.1213,14589]
LT=["MJ", 10.22, (2,"JM")]

#Changing a list

L.extend(["pop", 10])
print(L)
#to add new elements from a list in the list
L.append(["prob",12])
#to add a list in the list, or simple elements in a list
print(L)

L.append("A")
print(L)
#You can't add new elements in a list using .extend() Method, append is used for it.

Clone = L[:]
print(Clone)
#You can clone lists for manipulate them better, and not affecting the original.

# help(L)

# print([1,2,3] + [1,1,1])
# A=[]
# A.append([2,3,4,5])
# A=[1]
# print(A)

A=(1,2,3,4,5)
print(A[1:4])