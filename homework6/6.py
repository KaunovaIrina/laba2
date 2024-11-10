def get_number():
    """Генератор нечетных чисел из диапазона от 0 до 29."""
    for num in range(30):
        if num % 2 != 0:  # Проверка на нечетность
            yield num

def main():
    while True:
        user_input = input("Введите число для проверки (или 'exit' для выхода): ")
        
        # Проверка на корректность ввода
        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break
        
        if not user_input.isdigit():
            print("Ошибка: введите корректное число.")
            continue

        # Получаем генератор
        odd_numbers = list(get_number())
        
        # Печатаем первое, пятое и последнее значение, если они существуют
        try:
            print(f"Первое нечетное число: {odd_numbers[0]}")
            print(f"Пятое нечетное число: {odd_numbers[4]}")
            print(f"Последнее нечетное число: {odd_numbers[-1]}")
        except IndexError:
            print("Не хватает элементов в списке нечетных чисел.")

# Вызов основной функции
main()
