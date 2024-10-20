# import importlib
# importlib.reload(cars)

class Vehicle:
    def __init__(self, make, model, feul, num_wheels):
        self.make = make
        self.model = model
        self.feul = feul

# Add the class that you want to extend from;
class Car(Vehicle):
    def __init__(self, make, model, feul, num_wheels=4):
        # pass the super() + method + properties
        super().__init__(make, model, feul)
        self.num_wheels = num_wheels

three_whlr = Vehicle("mitsubishi", "Mizushima", "Gas", 3)
print(three_whlr)