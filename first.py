# Імпорт необхідних модулів
import json
import string
import random

# Функція генерації пароля
def generate_password(letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    chars = ''
    if letters:
        chars += string.ascii_letters
    if symbols:
        chars += "!@#$%^&*()+"
    if numbers:
        chars += string.digits
    if not duplicates:
        chars = ''.join(set(chars))
    return ''.join(random.choice(chars) for _ in range(pass_length))

# Функція створення нового запису з паролем
def create_new_record(database, title, login, letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    password = generate_password(letters, symbols, numbers, duplicates, pass_length)
    new_record = {'title': title, 'login': login, 'password': password}
    database.append(new_record)
    with open('database.json', 'w') as file:
        json.dump(database, file)
    print("Новий запис створено успішно.")

# Функція отримання пароля за полем title
def get_password(database, title):
    for record in database:
        if record['title'] == title:
            print("title:", record['title'])
            print("login:", record['login'])
            print("password:", record['password'])
            return
    print("Запис з таким заголовком не знайдено.")

# Функція завантаження бази даних
def load_database():
    try:
        with open('database.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Основна функція програми
def main():
    database = load_database()
    
    while True:
        print("\nМеню:")
        print("1. Створити новий запис з паролем")
        print("2. Отримати пароль за полем title")
        print("3. Вийти з програми")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            title = input("Введіть назву сервісу: ")
            login = input("Введіть логін: ")
            letters = input("Включити літери у паролі? (True/False): ").lower() == 'true'
            symbols = input("Включити символи у паролі? (True/False): ").lower() == 'true'
            numbers = input("Включити цифри у паролі? (True/False): ").lower() == 'true'
            duplicates = input("Дозволити дублікати символів у паролі? (True/False): ").lower() == 'true'
            pass_length = int(input("Введіть довжину паролю: "))
            create_new_record(database, title, login, letters, symbols, numbers, duplicates, pass_length)
        elif choice == '2':
            title = input("Введіть назву сервісу: ")
            get_password(database, title)
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
