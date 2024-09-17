from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

result_1 = list(map(lambda x, y: x == y, first, second))

print(result_1)


def get_advanced_writer(file_name):
    # Внутренняя функция для записи данных в файл
    def write_everything(*data_set):
        # Открываем файл в режиме добавления (append)
        with open(file_name, 'a', encoding='utf-8') as file:
            # Перебираем каждый элемент в data_set
            for data in data_set:
                # Преобразуем данные в строку и записываем их в файл
                file.write(str(data) + '\n')  # Записываем данные в файл с новой строки

    # Возвращаем функцию write_everything
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words):
        # Инициализируем атрибут words, который хранит коллекцию строк
        self.words = words

    # Метод __call__ позволяет вызывать объект как функцию
    def __call__(self):
        # Возвращаем случайное слово из коллекции words
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
