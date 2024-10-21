### Задание 5

# Написать программу, которая:

# - Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
# - Находит количество положительных, отрицательных и нулевых элементов в списке.
# - Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
# - Выводит самое большое и самое маленькое значение


import random # Импортируем модуль random для генерации случайных чисел


numbers = [random.randint(-50, 50) for _ in range(25)] # Создание списка из 25 случайных целых чисел в диапазоне от -50 до 50


positive_count = 0 # Инициализация счетчиков для положительных чисел
negative_count = 0 # Инициализация счетчиков для отрицательных чисел
zero_count = 0 # Инициализация счетчиков для нулевых чисел


for number in numbers: # Подсчет количества положительных, отрицательных и нулевых чисел в списке
    
    if number > 0:  # Если число положительное
        
        positive_count += 1 # + 1 в счетчик с положительными числами
        
    elif number < 0:  # Если число отрицательное
        
        negative_count += 1 # + 1 в счетчик с отрицательными числами
        
    else:  # Если число равно нулю
        
        zero_count += 1 # + 1 в счетчик с нулевыми числами

total_count = len(numbers)  # Общее количество чисел в списке
positive_percentage = (positive_count / total_count) * 100  # Процент положительных чисел
negative_percentage = (negative_count / total_count) * 100  # Процент отрицательных чисел
zero_percentage = (zero_count / total_count) * 100  # Процент нулевых чисел

max_value = max(numbers)  # Самое большое число
min_value = min(numbers)  # Самое маленькое число


print("Список сгенерированных чисел:")# Вывод списка чисел
print(numbers)  # Печатаем сам список

# Вывод результатов подсчета
print("\nПодсчеты:")
print(f"Количество положительных чисел: {positive_count} ({positive_percentage}%)")  # Результат для положительных
print(f"Количество отрицательных чисел: {negative_count} ({negative_percentage}%)")  # Результат для отрицательных
print(f"Количество нулей: {zero_count} ({zero_percentage}%)")  # Результат для нулевых чисел

# Вывод максимального и минимального значений
print(f"\nНаибольшее число в списке: {max_value}")  # Самое большое значение
print(f"Наименьшее число в списке: {min_value}")  # Самое маленькое значение