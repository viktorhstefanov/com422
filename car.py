class Car:

    def __init__(self, brand, colour, current_speed, max_speed, fuel_level):
        if fuel_level < 0 or fuel_level > 100:
            raise Exception("Fuel level must be between 0 and 100")

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
            return True
        elif self.fuel_level < 0:
            self.fuel_level = 0
            return True
        elif self.fuel_level == 0:
            self.current_speed = 0
            return True
        return False

    def brake(self, speed):
        self.current_speed = self.current_speed - speed
        if self.current_speed < 0:
            self.current_speed = 0
            return True
        return False

    def refuel(self, amount):
        self.fuel_level = self.fuel_level + amount
        if self.fuel_level > 100:
            self.fuel_level = 100
            return True
        return False

    def __str__(self):
        return (f"brand: {self.brand}, colour: {self.colour},"
                f" current speed: {self.current_speed}, max speed: {self.max_speed}, "
                f"fuel level: {self.fuel_level}")
