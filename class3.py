# def return_five(numbers):
#     result = []
#     for num in numbers:
#         if len(num) > 5:
#             result.append(num)
#     return result

# test_list = ["кот", "программирование", "дом", "привет", "a", "123456"]
# print(return_five(test_list))





# def get_short_names(names):
#     result = []

#     for num in names:
#         clean_names = num.strip().lower()
#         if len(clean_names) < 4:
#             result.append(clean_names)
#     return result


# names = ["  Анна  ", "Ким", "Джонатан", "  боб  ", "Ев", "МАКС"]
# print(get_short_names(names))


# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
        
     
# def get_avg_grades(student):
#         avg = sum(student.grades) / len(student.grades)
#         return avg
            

# def print_student_info(student):
#         avg = get_avg_grades(student)
#         print(f"Студент: {student.name}, Год: {student.age}, Средний балл: {avg}, Средний>4.1: {avg}")


# students = [
#       Student("Рома", 18, [5.0, 5.1]),
#       Student("Кирилл", 19, [4.0, 3.1]),
#       Student("Андрей", 20, [3.0, 2.1])
# ]

# for student in students:
#       avg = get_avg_grades(student)
#       if avg > 4.1:
#             print_student_info(student)
      

# print(get_avg_grades(student1))
# print(get_avg_grades(student2))
# print(get_avg_grades(student3))



# def get_weekday(n):
#     match n:
#         case 1:
#             return f"Понедельник"
#         case 2:
#             return f"Вторник"
#         case 3:
#             return f"Среда"
#         case 4:
#             return f"Четверг"
#         case 5:
#             return f"Пятница"
#         case 6:
#             return f"Суббота"
#         case 7:
#             return f"Воскресенье"
#         case _:
#             return f"Значение должно быть от 1 до 7"
        


# def get_weekday(n):
#     weekdays = [
#         "ПН",
#         "Вторник",
#         "Среда",
#         "Четверг",
#         "Пятница",
#         "Суббота",
#         "Воскресенье",
#     ]
#     if 1 <= n <= 7:
#         return weekdays [n - 1]
#     else:
#        return "Значение должно быть от 1 до 7"

# n = int(input("Введите число от 1 до 7: "))
# result = get_weekday(n)
# print(result)



def get_max_number():
    numbers = [
        0,
        1,
        2,
        3,
        4,
        5,
        16,
        7,
        8,
        9
    ]
    max_number = numbers[0]
    for n in numbers:
        if n > max_number:
            max_number = n
    print(max_number)

get_max_number()

#     for i in range(3): print(i)  # 0 1 2













