import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.total_enemies = 100  # У всех рыцарей по 100 врагов
        self.days = 0  # Счетчик дней сражения

    def run(self):
        # Сообщаем, что на рыцаря напали
        print(f"{self.name}, на нас напали!\n")

        # Пока есть враги, сражаемся
        while self.total_enemies > 0:
            time.sleep(1)  # Сражение идет 1 день (1 секунда)
            self.days += 1  # Увеличиваем счетчик дней

            # Уменьшаем количество врагов на значение силы рыцаря
            self.total_enemies -= self.power
            if self.total_enemies < 0:
                self.total_enemies = 0  # Убеждаемся, что врагов не меньше нуля

            # Выводим сообщение о текущем дне сражения и оставшихся врагах
            print(f"{self.name}, сражается {self.days} день(дня/дней)..., осталось {self.total_enemies} воинов.\n")

        # Когда все враги побеждены
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!\n")


# Создаем двух рыцарей с соответствующими параметрами
first_knight = Knight('Sir Lancelot', 10)  # Sir Lancelot уменьшает количество врагов на 10 каждый день
second_knight = Knight('Sir Galahad', 20)   # Sir Galahad уменьшает количество врагов на 20 каждый день

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ждем завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")
