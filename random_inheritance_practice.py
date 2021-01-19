class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def honk(self):
        return "Beep!"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # this is python3 specific!
        self.wheels = 4

my_wheels = Car("Honda","Odyssy",2003)
print(my_wheels.honk())