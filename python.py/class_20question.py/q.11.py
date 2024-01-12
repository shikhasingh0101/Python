class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"The {self.brand} is now in motion."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"The {self.brand} {self.model} is zooming down the road."

class Bicycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def drive(self):
        return f"The {self.brand} {self.type} is pedaling along."

# Example usage:
car_instance = Car("Toyota", "Camry")
bicycle_instance = Bicycle("Schwinn", "Mountain Bike")

# Accessing the drive method of Car instance
print(car_instance.drive())

# Accessing the drive method of Bicycle instance
print(bicycle_instance.drive())
