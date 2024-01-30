from car2 import Car


class CarPark:

    def __init__(self):
        self.cars = []

    def add_car(self):
        car = input()
        if len(self.cars) <= 15:
            self.cars.append(car)
        if len(self.cars) > 15:
            raise Exception("All spaces are full")

    def remove_car(self):
        car = input()
        self.cars.remove(car)

    def see_available_spaces(self):
        print(f"There are {len(self.cars)}spaces occupied and {15 - len(self.cars)} spaces free")



