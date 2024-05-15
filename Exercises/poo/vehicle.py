class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    
    def Fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def Fare(self):
        totalamount = super().Fare()
        totalamount += totalamount * 0.1
        return totalamount
    
class Car(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12, 50)
print(f"The total amount is: {school_bus.Fare():.2f}")
print(f"Base Class: {type(school_bus)}") # Write which class a given object belongs to
print(f"Is a Vehicle Instance: {isinstance(school_bus, Vehicle)}")