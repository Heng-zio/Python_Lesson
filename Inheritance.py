'''
Inheritance

superclass = parent class
subclass = child class

'''

class Animal:  #superclass
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound."
    
class Dog(Animal):  #subclass
    def __init__(self, name, breed):
        super().__init__(name)  #call the constructor of the superclass
        self.breed = breed

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak())  #inherited method
print(f"{my_dog.name} is a {my_dog.breed}.")