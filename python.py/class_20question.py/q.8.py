class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating a Car object
my_car = Car("Toyota", "Camry", 2022)

# Printing details of the Car object
print("Car Details:")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
