#Ecapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name      # private attribute
        self.__age = age        # private attribute

    def get_name(self):        # public method to access private attribute
        return self.__name

    def set_name(self, name):   # public method to modify private attribute
        self.__name = name

    def get_age(self):         # public method to access private attribute
        return self.__age

    def set_age(self, age):     # public method to modify private attribute
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")
# Create an object of the Person class
person = Person("Alice", 30)
print(person.get_name())  # Accessing private attribute via public method
print(person.get_age())   # Accessing private attribute via public method
person.set_age(35)        # Modifying private attribute via public method
print(person.get_age())
person.set_age(-5)       # Attempting to set a negative age
print(person.get_age())
person.set_name("Bob")    # Modifying private attribute via public method
print(person.get_name())
