class Car:

    def __init__(self, brand, colour, current_speed, max_speed, fuel_level):
        self.brand = brand
        self.colour = colour
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = fuel_level

    def accelerate(self, speed):
        self.current_speed = self.current_speed + speed
        self.fuel_level = self.fuel_level - speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.fuel_level < 0:
            self.fuel_level = 0
        if self.fuel_level == 0:
            self.current_speed = 0

    def brake(self, speed):
        self.current_speed = self.current_speed - speed
        if self.current_speed < 100:
            self.current_speed = 0

    def refuel(self, amount):
        self.fuel_level = self.fuel_level + amount
        if self.fuel_level > 100:
            self.fuel_level = 100

    def __str__(self):
        return (f"brand: {self.brand}, colour: {self.colour},"
                f" current speed: {self.current_speed}, max speed: {self.max_speed}, "
                f"fuel level: {self.fuel_level}")
