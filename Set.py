#Set

#my_set = {item1, item2, item3.....}

#Set can not store the same value like apple and apple in set

Fruits = {"apple", "banana", "cherry" , "apple" }

print(type(Fruits))

print(Fruits)

#adding items
Fruits.add("orange")

print(Fruits)

#union set1 and set2

set1 = { 4 , 5 , 6 }

set2 = { 1 , 2 , 3 }

print(set1.union(set2))

#intersection of set1 and set2
set3 = { 1 , 2 , 3 , 4 , 5 }

set4 = { 4 , 5 , 6 , 7 , 8 }

print(set3.intersection(set4))


#difference of set1 and set2
set5 = { 1 , 2 , 3 , 4 , 5 }

set6 = { 4 , 5 , 6 , 7 , 8 }

print(set5.difference(set6))

#symmetric difference of set1 and set2

set7 = { 1 , 2 , 3 , 4 , 5 }

set8 = { 4 , 5 , 6 , 7 , 8 }

print(set7.symmetric_difference(set8))