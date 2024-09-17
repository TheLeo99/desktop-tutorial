class StepValueError(ValueError):
    pass  # Наследуется от ValueError, класс остается пустым

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:  # Проверяем шаг итерации на равенство 0
            raise StepValueError('шаг не может быть равен 0')

        # Инициализируем атрибуты объекта
        self.start = start  # целое число с которого начинается итерация
        self.stop = stop  # целое число на котором заканчивается итерация
        self.step = step  # шаг с которым совершается итерация
        self.pointer = start  # Устанавливаем pointer (текущее число в итерации) на начальное значение

    # Метод __iter__ для сброса указателя и возвращения итератора
    def __iter__(self):
        self.pointer = self.start  # сбрасываает значение pointer на start
        return self  # возвращает сам объект итератора

    # Метод __next__ для итерации
    def __next__(self):  # метод, увеличивающий атрибут pointer на step
        # Для положительного шага проверяем, что pointer не превысил stop
        if self.step > 0 and self.pointer >= self.stop:
            raise StopIteration
        # Для отрицательного шага проверяем, что pointer не стал меньше stop
        elif self.step < 0 and self.pointer <= self.stop:
            raise StopIteration

        # Сохраняем текущее значение pointer
        current_value = self.pointer

        # Увеличиваем pointer на step
        self.pointer += self.step
        return current_value


#  Пример использования
try:
    iter1 = Iterator(100, 200, 0)  # Шаг 0 вызывает исключение
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Выполнение итерации для каждого объекта
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
