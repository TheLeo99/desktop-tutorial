n = int(input("Введите число от 3 до 20: "))

# Проверка ввода
if 3 <= n <= 20:
  result = ''
  for i in range(1, n):
    for j in range(i + 1, n + 1):
      if (i + j) % n == 0:
        result += str(i) + str(j)
  print(f"Пароль для числа {n}: {result}")
else:
  print("Некорректный ввод. Введите число от 3 до 20.")
