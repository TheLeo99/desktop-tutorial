class IncorrectVinNumber(Exception):
    def __init__(self, message="Некорректный vin номер"):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message="Некорректные номера автомобиля"):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__is_valid_vin(self.__vin)  # Проверка VIN при создании объекта
        self.__numbers = numbers
        self.__is_valid_numbers(self.__numbers)  # Проверка номеров при создании объекта

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):  # VIN должен быть целым числом
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:  # Проверка длины номеров
            raise IncorrectCarNumbers("Неверная длина номера")
        return True


# Пример использования
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')