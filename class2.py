class Lead:
    def __init__(self, name):
        self.name = name
    
    def change_name(self):  # self — ссылка на КОНКРЕТНЫЙ объект
        self.name = "Need"

# Создаем объект (экземпляр класса)
my_lead = Lead("Вася")
print(my_lead.name)  # Вася

# Меняем имя у ЭТОГО объекта
my_lead.change_name()
print(my_lead.name)  # Need ✅