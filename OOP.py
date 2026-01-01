class Car :
    #constructor method
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Create an object of the Car class
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
