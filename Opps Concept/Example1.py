#Create a Vehicle class with max_speed and mileage instance attribute

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
Model = Vehicle(240,18)
print(Model.max_speed,Model.mileage)