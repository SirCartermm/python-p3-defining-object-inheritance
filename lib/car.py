class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def description(self):
        return f"{self.year} {self.brand} {self.model}"

    def mileage_counter(self, miles):
        self.mileage += miles


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def description(self):
        desc = super().description()
        return f"{desc} with {self.doors} doors"