class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}")
    
    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model
    
    def to_dict(self):
        return {"brand": self.brand, "model": self.model, "year": self.year}