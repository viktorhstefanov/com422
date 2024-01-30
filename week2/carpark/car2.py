class Car:
    def __init__(self, brand, reg_number):
        self.brand = brand
        self.reg_number = reg_number

    def __str__(self):
        return f"brand: {self.brand}, registration number: {self.reg_number}"
