import random

def find_multiples():
    # Генерация списка случайных чисел
    numbers = [random.randint(0, 200) for _ in range(10)]
    print(f"Сгенерированные числа: {numbers}")
    
    while True:
        x_input = input("Введите цифру X (от 1 до 9): ")
        
        # Проверка на корректность ввода
        if x_input.isdigit() and 1 <= int(x_input) <= 9:
            x = int(x_input)
            break
        else:
            print("Ошибка: введите корректную цифру от 1 до 9.")
    
    # Использование лямбда-функции для фильтрации чисел
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    if multiples:
        print(f"Числа, кратные {x}: {multiples}")
    else:
        print(f"Нет чисел, кратных {x}.")

# Вызов функции
find_multiples()
