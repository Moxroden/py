import random
import time




class LoopsPractice:
    def number_list_task(self):
        numbers = list(range(1, 8))
        for num in numbers:
         print(num)
         if num == 5:
            break
         

    def string_list_task(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
           print(word)

    def load_monitoring(self):
       counter = 0
       while counter < 10:
          load = random.randint(0, 100)
          print(f"Нагрузка: {load}%")
          if load > 85:
             print("⚠️ Предупреждение! Высокая нагрузка!")
          time.sleep(0.2)
          counter += 1

if __name__ == "__main__":
    tasks = LoopsPractice()
    tasks.number_list_task()
    tasks.string_list_task()
    tasks.load_monitoring()