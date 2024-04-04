# Superclass: Vehicle
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def go(self):
        return "The vehicle is moving."

# Subclass: Car
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def go(self):
        return super().go() + " Vroom, vroom!"

# Create a Car object
car = Car("Toyota", "Camry", 2023)

# Print the car's make, model, and year
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")

# Call the go() method
print(car.go())
