from math import sqrt, ceil

def baby_step_giant_step(a, y, p, verbose=True):
    mult_count = 0

    if verbose:
        print(f"\nМЕТОД ШЭНКСА")
        print("-" * 50)

    m = k = ceil(sqrt(p))
    if verbose:
        print(f"1. m = k = ceil(√{p}) = {m}")
        print(f"Проверка: m*k = {m * k} > {p}? {'Да' if m * k > p else 'Нет'}")

    baby_steps = {}
    current = y
    baby_steps[current] = 0
    if verbose:
        print(f"\n2. Baby Steps (j=0..{m - 1}):")
        print(f"   j=0: {y}*{a}^0 mod {p} = {current}")

    for j in range(1, m):
        current = (current * a) % p
        mult_count += 1
        baby_steps[current] = j
        if verbose:
            print(f"   j={j}: {y}*{a}^{j} mod {p} = {current}")

    a_m = pow(a, m, p)
    mult_count += m.bit_length()

    if verbose:
        print(f"\n3. Giant Steps (i=1..{k}):")
        print(f"   Вычисляем {a}^{m} mod {p} = {a_m}")

    current = a_m
    if verbose:
        print(f"   i=1: ({a}^{m})^1 mod {p} = {current}")

    if current in baby_steps:
        j = baby_steps[current]
        x = (1 * m - j) % (p - 1)
        if verbose:
            print("\n   НАЙДЕНО ПЕРВОЕ СОВПАДЕНИЕ:")
            print(f"   При i=1, j={j}:")
            print(f"   {a}^{m} mod {p} = {current}")
            print(f"   {y}*{a}^{j} mod {p} = {current}")
            print(f"   Решение: x = 1*{m} - {j} = {x}")
            print(f"   Проверка: {a}^{x} mod {p} = {pow(a, x, p)}")
            print(f"   Всего умножений: {mult_count}")
        return x, mult_count

    for i in range(2, k + 1):
        current = (current * a_m) % p
        mult_count += 1
        if verbose:
            print(f"   i={i}: ({a}^{m})^{i} mod {p} = {current}")

        if current in baby_steps:
            j = baby_steps[current]
            x = (i * m - j) % (p - 1)
            if verbose:
                print("\n   НАЙДЕНО СОВПАДЕНИЕ:")
                print(f"   При i={i}, j={j}:")
                print(f"   {a}^{i * m} mod {p} = {current}")
                print(f"   {y}*{a}^{j} mod {p} = {current}")
                print(f"   Решение: x = {i}*{m} - {j} = {x}")
                print(f"   Проверка: {a}^{x} mod {p} = {pow(a, x, p)}")
                print(f"   Всего умножений: {mult_count}")
            return x, mult_count

    if verbose:
        print("\nСовпадений не найдено!")
    return None, mult_count

def brute_force(a, y, p, verbose=True):
    mult_count = 0

    if verbose:
        print(f"\nМЕТОД ПЕРЕБОРА")
        print("-" * 50)

    current = 1
    if current == y:
        if verbose:
            print(f"   Найдено решение при x=0")
            print(f"   Всего умножений: 0")
        return 0, 0

    for x in range(1, p):
        current = (current * a) % p
        mult_count += 1
        if verbose:
            print(f"   x={x}: {a}^{x} mod {p} = {current}")

        if current == y:
            if verbose:
                print(f"   Найдено решение при x={x}")
                print(f"   Всего умножений: {mult_count}")
            return x, mult_count

    return None, mult_count

def solve(a, y, p):
    print("\n" + "=" * 60)
    print(f"РЕШЕНИЕ УРАВНЕНИЯ: {a}^x mod {p} = {y} ")
    print("=" * 60)

    x_bsgs, ops_bsgs = baby_step_giant_step(a, y, p, verbose=True)
    x_brute, ops_brute = brute_force(a, y, p, verbose=True)

    print("\n" + "-" * 60)
    print("СРАВНЕНИЕ МЕТОДОВ:")
    print(f"Метод Шэнкса: x = {x_bsgs}, умножений = {ops_bsgs}")
    print(f"Метод перебора: x = {x_brute}, умножений = {ops_brute}")

    if ops_brute < ops_bsgs:
        ratio = ops_bsgs / ops_brute
        print(f"\nВЫВОД: Метод перебора быстрее в {ratio:.1f} раз")
    else:
        ratio = ops_brute / ops_bsgs
        print(f"\nВЫВОД: Метод Шэнкса быстрее в {ratio:.1f} раз")


solve(2, 9, 23)
solve(2, 100, 1009)