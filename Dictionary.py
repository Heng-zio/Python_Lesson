#Dictionary
#Keys are unique and immutable, and values can be any type
#my_dict = {key1: value1, key2: value2, key3: value3}

person = {"name": "MiLyHeng" , "age" : 19 }

print(person["name"])

print(person["age"])

#adding items
person["job"] = "deverloper"

print(person)

#updating items
person["age"] = 100

print(person)

#delete items
del person["job"]

print(person)

#To get keys
print(person.keys())

#to update the whole dictionary
person.update({"name": "Joyboy" , "age" : 20})

print(person)

#to clear the dictionary
person.clear()

print(person)  #This will print empty dictionary because we clear it