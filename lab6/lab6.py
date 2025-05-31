def fast_exp(a, x, p):
    y = 1
    s = a
    multiplications = 0
    binary_x = bin(x)[2:]
    print(f"\nДвоичное представление x: {binary_x}")
    print("\nТрассировка вычислений:")
    print(f"{'Шаг':<5} | {'Бит':<5} | {'y (до)':<10} | {'s (до)':<10} | {'Действие':<20} | {'s(после)':<10} | {'Умножение'}")
    print("-" * 85)

    step = 0
    for bit in reversed(binary_x):
        x_i = int(bit)
        print(f"{step:<5} | {x_i:<5} | {y:<10} | {s:<10} | ", end="")

        if x_i == 1:
            y = (y * s) % p
            multiplications += 1
            action = f"y = y*s = {y}"
            print(f"{action:<20} | ", end="")
        else:
            print(f"{'Пропускаем':<20} | ", end="")

        s = (s * s) % p
        multiplications += 1
        print(f"{s:<10} | {multiplications}")
        step += 1

    print(f"\nРезультат: {a}^{x} mod {p} = {y}")
    print(f"Общее количество умножений: {multiplications}")
    return y


def main():
    print("Введите параметры для вычисления a^x mod p:")
    a = int(input("Основание (a): "))
    x = int(input("Показатель степени (x): "))
    p = int(input("Модуль (p): "))
    fast_exp(a, x, p)


if __name__ == "__main__":
    main()

