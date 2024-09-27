import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом, по умолчанию None
        self.lock = threading.Lock()  # Блокировка для безопасности потока

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()  # Инициализация базового класса Thread
        self.name = name  # Имя гостя

    def run(self):
        wait_time = random.randint(3, 10)  # Случайное время ожидания от 3 до 10 секунд
        time.sleep(wait_time)  # Имитация времени пребывания за столом

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = list(tables)  # Список столов

    def guest_arrival(self, *guests):  # Приём гостей
        for guest in guests:  # Ищем свободный стол
            seated = False
            for table in self.tables:
                if table.lock.acquire(blocking=False):  # Блокировка
                    if table.guest is None:  # Если стол свободен
                        table.guest = guest  # Сажаем гостя за стол
                        print(f"{guest.name} сел(-а) за стол номер {table.number}.")
                        guest.start()  # Запускаем поток гостя (начало еды)
                        seated = True
                        break
                    table.lock.release()  # Снятие блокировки, если стол занят

            if not seated:  # Если нет свободных столов, добавляем гостя в очередь
                print(f"{guest.name} в очереди.")
                self.queue.put(guest)

    def discuss_guests(self):  # Обслуживание гостей
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(-ушла).")
                    print(f"Стол номер {table.number} свободен.")
                    table.guest = None  # Освобождаем стол
                    table.lock.release()

                    if not self.queue.empty():  # Если очередь не пуста
                        next_guest = self.queue.get()  # Приглашаем следующего гостя из очереди
                        if table.lock.acquire(blocking=False):  # Блокировка
                            table.guest = next_guest  # Сажаем гостя за стол
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.")
                            next_guest.start()  # Запускаем поток следующего гостя
                        else:
                            self.queue.put(next_guest)  # Если не удается получить блокировку, сажаем гостя обратно в очередь

            time.sleep(1)  # Пауза

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

# Дожидаемся завершения потоков
for guest in guests:
    guest.join()
