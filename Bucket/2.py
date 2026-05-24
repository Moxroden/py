import requests

def get_user_name(user_id: int) -> str:
    # Делаем GET-запрос к API
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    
    # Проверяем, что запрос успешен (статус код 200)
    if response.status_code == 200:
        # Преобразуем ответ в JSON и берем поле 'name'
        user_data = response.json()
        return user_data['name']
    else:
        # Если что-то пошло не так, возвращаем ошибку
        return f"Ошибка: статус код {response.status_code}"

print(get_user_name(1))