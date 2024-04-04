# Class: Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "The engine is starting."

# Class: Car
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def go(self):
        return f"The {self.make} {self.model} is moving. {self.engine.start()}"

# Create a Car object with an Engine object
car = Car("Toyota", "Camry", Engine(200))

# Print the car's make, model, and engine horsepower
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Engine Horsepower: {car.engine.horsepower}")

# Call the go() method
print(car.go())
