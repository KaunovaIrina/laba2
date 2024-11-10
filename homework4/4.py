from datetime import datetime

def calculate_age():
    while True:
        birth_date_input = input("Введите вашу дату рождения в формате ДД/ММ/ГГГГ: ")
        
        # Проверка на корректность формата даты
        try:
            birth_date = datetime.strptime(birth_date_input, "%d/%m/%Y")
            break  # Если дата введена корректно, выходим из цикла
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате ДД/ММ/ГГГГ.")
    
    today = datetime.today()
    age = today.year - birth_date.year
    
    # Проверка, прошел ли день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    print(f"Ваш возраст: {age} лет.")

# Вызов функции
calculate_age()
