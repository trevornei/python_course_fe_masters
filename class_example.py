

class Vehicle:
    def __init__(self, make, model, fuel="gas", num_wheels=4):
        self.make = make
        self.model = model
        self.fuel = fuel 
        self.num_wheels = num_wheels

    def __str__(self):
        # str's methods need a return statement.
        return f"My daily runner is a {self.make} {self.model}. It runs on {self.fuel}"

class Car(Vehicle):

    number_of_wheels = 4

class Truck(Vehicle):

    number_ofwheels = 8
    def __init__(self, make, model, fuel="Diesel",):
        super().__init__(self, make, model, fuel) 


daily = Vehicle("Toyota", "4Runner")
print(daily)

print("for Class", daily.num_wheels)