# import importlib
# from cars import Car
# make sure to import cars itself so reload.(cars) knows to reference cars.
# import cars
# importlib.reload(cars)

class Car:
    runs = True
    number_of_wheels = 4

    # Create special methods...
    # Create a constructor method...
    # Create fn, use dunder init dunder ()
    def __init__(self, name, year, owner):
        self.name = name
        self.year = year
        self.owner = owner

    # Now, we'll create a string representation of this instance!
    def __str__(self):
        return f"My car: {self.name},\n Year built: {self.year},\n Owner of the Vehicle: {self.owner}\n"
    
    def start(self):
        # Self is associated with the instance of the class.
        # Remember in JS 'this.' is the equivalent of self.
        if self.runs:
            print(f"Your {self.name} has started.")
        else:
            print(f"Your {self.name} is not working ah akashd foahsodfhalsdf oasdf.")

# Class methods = @
# @classmethods don't take the arguments of self but rather 'cls'
@classmethod 
def get_number_of_wheels(cls):
# Declare return statement...
    return cls.number_of_wheels

subaru = Car("Outback", "2016", "Trevor")
tesla = Car("Model X", "2025", "Sam")
ford = Car("F-150", "2022", "Paul")

print(f"Vehicle One: {subaru}\n Vehicle One: {tesla}\n Vehicle One: {ford}\n")