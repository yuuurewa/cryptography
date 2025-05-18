import nltk.corpus as nc

def caesar_encrypt(text: str, key: int) -> str:
    encrypted = []
    for char in text:
        if char.isalpha():
            shifted = (ord(char.lower()) - ord('a') + key) % 26
            encrypted.append(chr(shifted + ord('a')))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def caesar_decrypt(text: str, key: int) -> str:
    return caesar_encrypt(text, -key)

def find_key(plaintext: str, ciphertext: str) -> int:
    if len(plaintext) == 0 or len(ciphertext) == 0:
        return 0
    p_char = plaintext[0].lower()
    c_char = ciphertext[0].lower()
    if not p_char.isalpha() or not c_char.isalpha():
        return 0
    return (ord(c_char) - ord(p_char)) % 26

def brute_force_caesar(ciphertext: str):
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        print(f"Ключ {key}: {decrypted}")

def auto_decrypt(ciphertext: str) -> int:
    word_set = set(nc.words.words())
    best_key = 0
    max_matches = 0
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        decrypted_words = decrypted.split()
        matches = sum(word.lower() in word_set for word in decrypted_words)
        if matches > max_matches:
            max_matches = matches
            best_key = key
    return best_key

def main():
    print("Меню:")
    print("1. Зашифровать текст")
    print("2. Расшифровать текст")
    print("3. Атака по известному тексту")
    print("4. Полный перебор ключей")
    print("5. Автоматическая расшифровка")
    print("0. Выход")

    while True:
        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            text = input("Введите текст для шифрования: ")
            key = int(input("Введите ключ (0-25): "))
            print(f"Зашифрованный текст: {caesar_encrypt(text, key)}")

        elif choice == "2":
            text = input("Введите текст для расшифровки: ")
            key = int(input("Введите ключ (0-25): "))
            print(f"Расшифрованный текст: {caesar_decrypt(text, key)}")

        elif choice == "3":
            plaintext = input("Введите известный исходный текст: ")
            ciphertext = input("Введите зашифрованный текст: ")
            key = find_key(plaintext, ciphertext)
            print(f"Найденный ключ: {key}")

        elif choice == "4":
            ciphertext = input("Введите зашифрованный текст для перебора: ")
            brute_force_caesar(ciphertext)

        elif choice == "5":
            ciphertext = input("Введите зашифрованный текст для авторасшифровки: ")
            key = auto_decrypt(ciphertext)
            decrypted = caesar_decrypt(ciphertext, key)
            print(f"Наиболее вероятный ключ: {key}")
            print(f"Расшифрованный текст: {decrypted}")

        elif choice == "0":
            print("Вы вышли из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()