from lib.car import Car

def test_car_description():
    my_car = Car("Toyota", "Corolla", 2015, 4)
    assert my_car.description() == "2015 Toyota Corolla with 4 doors"