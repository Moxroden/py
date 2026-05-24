class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}")


cars = [
    Car("bmw", "X5", 2023),
    Car("audi", "A4", 2022),
    Car("toyota", "Camry", 2021)
]

for car in cars:
    car.print_car_info()