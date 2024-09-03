def add_everything_up(a, b):

    try:
        return a + b  # Пытаемся выполнить сложение
    except TypeError:
        return str(a) + str(b)  # Если возникла ошибка TypeError, конкатенируем строки


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
