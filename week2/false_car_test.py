import pytest
from car import Car


def test_car_acceleration_false():
    car1 = Car("kia", "red", 50, 150, 70)
    assert car1.accelerate(20) == False


def test_car_brake_false():
    car1 = Car("kia", "red", 50, 150, 70)
    assert car1.brake(40) == False


def test_car_refuel_false():
    car1 = Car("kia", "red", 50, 150, 70)
    assert car1.refuel(25) == False


def test_car_raise_exception():
    with pytest.raises(Exception) as ex:
        car1 = Car("kia", "red", 50, 150, 70)
        assert str(ex.value) == "Fuel level must be between 0 and 100"



