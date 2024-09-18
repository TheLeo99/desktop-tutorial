def is_prime(func):
    # Декоратор для проверки простоты числа
    def wrapper(*args):
        result = func(*args)  # Вызов функции sum_three
        if result < 2:
            print("Составное")  # Числа меньше 2 не считаются простыми
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result  # Возвращаем результат функции
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример:
result = sum_three(2, 3, 6)
print(result)
