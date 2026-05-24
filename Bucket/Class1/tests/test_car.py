# import pytest
# from core.car import Car
# from utils.json_loader import load_cars_from_json

# class TestCar:
    
#     @pytest.fixture
#     def test_cars(self):
#         """Загружаем данные перед каждым тестом"""
#         return load_cars_from_json()
    
#     def test_all_cars_have_valid_year(self, test_cars):
#         """Проверяем, что год выпуска не в будущем"""
#         for car in test_cars:
#             assert car.year <= 2025, f"{car.brand} {car.model}: год слишком большой"
#             assert car.year >= 2000, f"{car.brand} {car.model}: год слишком маленький"
    
#     def test_car_info_format(self, test_cars):
#         """Проверяем формат вывода"""
#         for car in test_cars:
#             info = car.get_car_info()
#             assert car.brand in info
#             assert car.model in info
#             assert str(car.year) in info
    
#     @pytest.mark.parametrize("brand,model,year", [
#         ("bmw", "X5", 2023),
#         ("audi", "A4", 2022)
#     ])
#     def test_create_car_dynamically(self, brand, model, year):
#         """Параметризованный тест - без JSON"""
#         car = Car(brand, model, year)
#         assert car.brand == brand