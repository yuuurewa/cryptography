from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_file(input_file, output_file, key):
    # Проверка длины ключа (DES требует ровно 8 байт)
    if len(key) != 8:
        print("Ошибка: ключ должен быть ровно 8 символов!")
        return

    # Генерация IV (Initialization Vector)
    iv = os.urandom(8)

    # Создание объекта шифра
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)

    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Шифрование с дополнением данных
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    # Сохранение IV и зашифрованных данных
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

    print(f"Файл зашифрован: {output_file}")


def decrypt_file(input_file, output_file, key):
    # Проверка длины ключа
    if len(key) != 8:
        print("Ошибка: ключ должен быть ровно 8 символов!")
        return

    with open(input_file, 'rb') as f:
        data = f.read()

    # Извлечение IV и зашифрованных данных
    iv = data[:8]
    ciphertext = data[8:]

    # Создание объекта дешифратора
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)

    try:
        # Расшифрование и удаление дополнения
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

        with open(output_file, 'wb') as f:
            f.write(plaintext)

        print(f"Файл расшифрован: {output_file}")
    except ValueError:
        print("Ошибка: неверный ключ или повреждённый файл!")


def main():
    while True:
        print("\nМеню: ")
        print("1. Зашифровать файл")
        print("2. Расшифровать файл")
        print("3. Выход")
        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            input_file = input("Входной файл: ")
            output_file = input("Выходной файл: ")
            key = input("Ключ (ровно 8 символов): ")
            encrypt_file(input_file, output_file, key)

        elif choice == "2":
            input_file = input("Входной файл: ")
            output_file = input("Выходной файл: ")
            key = input("Ключ (ровно 8 символов): ")
            decrypt_file(input_file, output_file, key)

        elif choice == "3":
            print("Выход из программы")
            break

        else:
            print("Неверный выбор!")

        input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()
