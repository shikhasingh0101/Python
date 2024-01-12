class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        # Call the parent class method to get the base fare
        base_fare = super().calculate_fare()
        
        # Calculate maintenance charge for Bus instance (10% of base fare)
        maintenance_charge = 0.1 * base_fare
        
        # Total fare for Bus instance
        total_fare = base_fare + maintenance_charge
        
        return total_fare

# Example usage:
vehicle = Vehicle(50)
bus = Bus(50)

print(f"Vehicle Fare: ${vehicle.calculate_fare()}")
print(f"Bus Fare: ${bus.calculate_fare()}")
