def all_variants(text):
    # Внешний цикл перебирает начальные позиции подстрок
    for start in range(len(text)):
        # Внутренний цикл перебирает длину подстрок начиная с 1 до конца строки
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]  # Возвращаем подпоследовательность

# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
