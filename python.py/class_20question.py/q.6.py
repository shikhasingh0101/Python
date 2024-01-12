# class Vehicle:
#     # Class attribute with default value
#     color = "white"

#     def __init__(self, capacity):
#         self.capacity = capacity

#     def calculate_fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def calculate_fare(self):
#         base_fare = super().calculate_fare()
#         maintenance_charge = 0.1 * base_fare
#         total_fare = base_fare + maintenance_charge
#         return total_fare

# # Example usage:
# vehicle = Vehicle(50)
# bus = Bus(50)

# # Accessing the class attribute "color"
# print(f"Vehicle Color: {vehicle.color}")
# print(f"Bus Color: {bus.color}")
class Vehicle:
    # Class attribute with default value
    color = "white"

    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.1 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage:
vehicle = Vehicle(50)
bus = Bus(50)

# Accessing the class attribute "color"
print(f"Vehicle Color: {vehicle.color}")
print(f"Bus Color: {bus.color}")
