from .vehicle import vehicle

class Car(vehicle);
    def __init__(self, wheel_size, wheel_number):
        super().__init__(wheel_size, wheel_number)

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
