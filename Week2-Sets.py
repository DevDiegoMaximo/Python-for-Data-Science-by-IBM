#Sets
Set1= {"Rock", "Disco", "eletro", "pop", "Rock"}
#This is a Set

LT = ["Rock", 2, "pop", 2, "pop", "indie", "folk", "Rock"]
print(LT)
LT_Set = set(LT)
print(LT_Set)
#Converting a List into a Set.
#There are no duplicated elements in a Set.

A = {"AC/DC", "Back in Black", "NSYNC", "Thriller"}
A.add("NSYNC")
print(A)
#Add elements in a Set
A.remove("NSYNC")
print(A)
#remove a element in a set

album_set1 = {"AC/DC","Back in Black", "Thriller"}
album_set2 = {"AC/DC","Back in Black", "The Dark side of the moon"}
album_set3 = album_set1 & album_set2
print(album_set3) 
#The intersection between 2 Sets is made by the '&'. This catchs the same elements between 2 sets.

album_set1.union(album_set2)
#This results in the union of both sets.
print(album_set1)
