import pytest
from car import Car


def test_car_acceleration():
    car1 = Car("kia", "red", 50, 150, 70)
    car1.accelerate(10)
    assert car1.current_speed == 60
    assert car1.fuel_level == 60


def test_car_refuel():
    car1 = Car("kia", "red", 50, 150, 70)
    car1.refuel(20)
    assert car1.fuel_level == 90


def test_car_brake():
    car1 = Car("kia", "red", 50, 150, 70)
    car1.brake(30)
    assert car1.current_speed == 20





