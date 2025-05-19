import math
import os
import random
from collections import Counter


def calculate_frequencies(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    total_chars = len(data)
    frequencies = Counter(data)
    return {char: count / total_chars for char, count in frequencies.items()}


def calculate_entropy(frequencies):
    entropy = 0.0
    for freq in frequencies.values():
        if freq > 0:
            entropy -= freq * math.log2(freq)
    return entropy


def generate_file(file_path, file_type, size=1024, char=None):
    if file_type == 1:
        if not char:
            char = input("Введите символ для повторения: ")[0]
        data = char.encode() * size
    elif file_type == 2:
        data = ''.join(random.choice('01') for _ in range(size)).encode()
    elif file_type == 3:
        data = bytes([random.randint(32, 126) for _ in range(size)])
    elif file_type == 4:
        text = " ".join(["hello"] * (size // 6))
        data = text.encode()[:size]
    elif file_type == 5:
        text = " ".join(["привет"] * (size // 7))
        data = text.encode()[:size]

    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"Файл {file_path} успешно создан ({size} байт)")


def main_menu():
    print("\nМеню: ")
    print("1. Анализировать существующий файл")
    print("2. Сгенерировать тестовый файл")
    print("0. Выход")


def file_analysis_menu():
    file_path = input("Введите путь к файлу: ")

    if not os.path.exists(file_path):
        print("Ошибка: файл не существует")
        return

    try:
        frequencies = calculate_frequencies(file_path)
        entropy = calculate_entropy(frequencies)

        print("\nРезультаты анализа:")
        print(f"Размер файла: {os.path.getsize(file_path)} байт")
        print(f"Уникальных символов: {len(frequencies)}")
        print(f"Энтропия: {entropy:.4f} бит/символ")

    except Exception as e:
        print(f"Ошибка при анализе файла: {e}")


def generate_file_menu():
    print("1. Файл из повторяющегося символа")
    print("2. Случайные '0' и '1'")
    print("3. Случайные печатаемые ASCII-символы")
    print("4. Текст на английском")
    print("5. Текст на русском")

    choice = input("\nВыберите тип файла (1-5): ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Неверный выбор")
        return

    file_path = input("Введите имя файла для сохранения: ")
    size = input("Введите размер файла в байтах (по умолчанию 1024): ")
    try:
        size = int(size) if size else 1024
    except ValueError:
        print("Некорректный размер, будет использовано 1024 байта")
        size = 1024

    generate_file(file_path, int(choice), size)


def main():
    while True:
        main_menu()
        choice = input("\nВыберите действие: ")

        if choice == '1':
            file_analysis_menu()
        elif choice == '2':
            generate_file_menu()
        elif choice == '0':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор, попробуйте снова")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()