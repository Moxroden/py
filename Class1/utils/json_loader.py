import json
import os

def load_cars_from_json(file_path="data/cars.json"):
    """Загружает машины из JSON файла"""
    # Получаем абсолютный путь
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, file_path)
    
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    from core.car import Car
    
    cars = []
    for car_data in data["test_cars"]:
        car = Car(car_data["brand"], car_data["model"], car_data["year"])
        cars.append(car)
    
    return cars