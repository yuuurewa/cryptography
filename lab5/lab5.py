import hashlib
import os
from typing import Tuple, Dict


class SimpleAuthSystem:
    def __init__(self):
        self.users: Dict[str, Tuple[bytes, bytes]] = {}

    def _hash_password(self, password: str, salt: bytes = None) -> Tuple[bytes, bytes]:
        if salt is None:
            salt = os.urandom(16)
        hasher = hashlib.sha256()
        hasher.update(salt + password.encode('utf-8'))
        return salt, hasher.digest()

    def register_user(self, username: str, password: str) -> None:
        if username in self.users:
            raise ValueError("Пользователь уже существует")
        salt, hashed = self._hash_password(password)
        self.users[username] = (salt, hashed)
        print(f"Пользователь {username} успешно зарегистрирован!")

    def authenticate(self, username: str, password: str) -> bool:
        if username not in self.users:
            return False
        salt, stored_hash = self.users[username]
        _, hashed = self._hash_password(password, salt)
        return hashed == stored_hash


def main():
    auth_system = SimpleAuthSystem()
    try:
        auth_system.register_user("alice", "AlicePassword123")
        auth_system.register_user("bob", "BobSecurePass")
        auth_system.register_user("charlie", "Charlie123!")
    except ValueError as e:
        print(e)

    while True:
        print("\nМеню:")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            try:
                auth_system.register_user(username, password)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")

            if auth_system.authenticate(username, password):
                print(f"Добро пожаловать, {username}! Аутентификация успешна.")
            else:
                print("Ошибка: Неверное имя пользователя или пароль.")

        elif choice == "3":
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")


if __name__ == "__main__":
    main()
