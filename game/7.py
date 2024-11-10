import random

def get_user_choice():
    """Запрашивает выбор пользователя и проверяет корректность ввода."""
    while True:
        user_input = input("Введите 'камень', 'ножницы' или 'бумага' (или 'exit' для выхода): ").lower()
        if user_input in ['камень', 'ножницы', 'бумага']:
            return user_input
        elif user_input == 'exit':
            print("Выход из игры.")
            exit()
        else:
            print("Ошибка: введите корректный вариант ('камень', 'ножницы' или 'бумага').")

def get_computer_choice():
    """Случайно выбирает вариант для компьютера."""
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    """Определяет победителя."""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
        (user_choice == 'камень' and computer_choice == 'ножницы') or 
        (user_choice == 'ножницы' and computer_choice == 'бумага') or 
        (user_choice == 'бумага' and computer_choice == 'камень')
    ):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"



def main():
    print("Добро пожаловать в игру 'Камень-ножницы-бумага'!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

# Запуск игры
if __name__ == "__main__":
    main()
