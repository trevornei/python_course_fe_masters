class Car:
    runs = True

    def start(self, name):
        # Self is associated with the instance of the class.
        # Remember in JS 'this.' is the equivalent of self.
        self.name = name
        if self.runs:
            print(f"Your {self.name} has started.")
        else:
            print(f"Your {self.name} is not working ah akashd foahsodfhalsdf oasdf.")