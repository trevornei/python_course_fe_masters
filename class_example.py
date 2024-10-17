

class Vehicle:
    def __init__(self, make, model, feul="gas"):
        self.make = make
        self.model = model
        self.fuel = feul

daily = Vehicle("Toyota", "4Runner")
# print(daily_vehicle)

# print with f string.
print(f"I drive a {daily.make} {daily.model} as a daily driver.")