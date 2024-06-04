import unittest
from lib.car import Car

class TestCar(unittest.TestCase):
    def test_car_instantiation(self):
        car = Car(16, 4)
        self.assertIsInstance(car, Car)

    def test_car_go(self):
        car = Car(16, 4)
        self.assertEqual(car.go(), "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!")

if __name__ == '__main__':
    unittest.main()