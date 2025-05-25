import os


def create_text_file(file_path):
    print("\nВведите текст для сохранения в файл (дважды Enter для завершения):")
    text = []
    while True:
        line = input()
        if line == "":
            break
        text.append(line)

    full_text = '\n'.join(text)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"\nТекст сохранён в файл: {file_path} ({len(full_text)} символов)")


def generate_key(file_path, size):
    key = os.urandom(size)
    with open(file_path, 'wb') as f:
        f.write(key)
    print(f"Ключ сгенерирован: {file_path} ({size} байт)")


def vernam_cipher(input_file, key_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    with open(key_file, 'rb') as f:
        key = f.read()

    if len(data) > len(key):
        raise ValueError("Ошибка: ключ должен быть не короче данных!")

    result = bytes([a ^ b for a, b in zip(data, key)])

    with open(output_file, 'wb') as f:
        f.write(result)
    print(f"Результат сохранён в {output_file}")


class SimpleRC4:
    def __init__(self, key):
        self.S = list(range(256))
        j = 0

        for i in range(256):
            j = (j + self.S[i] + key[i % len(key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
        self.i = self.j = 0

    def encrypt(self, data):
        result = []
        for byte in data:
            self.i = (self.i + 1) % 256
            self.j = (self.j + self.S[self.i]) % 256
            self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
            k = self.S[(self.S[self.i] + self.S[self.j]) % 256]
            result.append(byte ^ k)
        return bytes(result)

def main_menu():
    print("\nМеню: ")
    print("1. Создать текстовый файл")
    print("2. Сгенерировать ключ")
    print("3. Шифр Вернама")
    print("4. Шифрование RC4")
    print("0. Выход")


def main():
    while True:
        main_menu()
        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            file_path = input("Введите имя файла для сохранения: ")
            create_text_file(file_path)

        elif choice == "2":
            file_path = input("Имя файла для ключа: ")
            size = int(input("Размер ключа (байт): "))
            generate_key(file_path, size)

        elif choice == "3":
            input_file = input("Файл с данными: ")
            key_file = input("Файл с ключом: ")
            output_file = input("Выходной файл: ")
            try:
                vernam_cipher(input_file, key_file, output_file)
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            input_file = input("Файл с данными: ")
            key = input("Ключ (строка): ").encode('utf-8')
            output_file = input("Выходной файл: ")

            with open(input_file, 'rb') as f:
                data = f.read()

            cipher = SimpleRC4(key)
            result = cipher.encrypt(data)

            with open(output_file, 'wb') as f:
                f.write(result)
            print(f"Результат сохранён в {output_file}")

        elif choice == "0":
            print("Выход из программы")
            break

        else:
            print("Неверный выбор!")

        input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()
