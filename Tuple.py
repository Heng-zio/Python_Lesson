#If List you can use index access and chang the value but if tuple you can not change the value because tuple
#The same list but use ()
number = (1,2,3,4,5)
fruit = ('apple', 'banana', 'cherry')
print(number)
print(fruit)
#If single element use (number , ) on it because you not use it will be simple integer
single_element = (5,)
print(single_element)
print(type(single_element))


#Acess index
fruit [0] = 'orange' #This will give error because tuple is immutable
print(fruit[0])