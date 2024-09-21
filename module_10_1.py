import threading
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')  # Запись строки в файл
            sleep(0.1)  # Пауза на 0.1 секунды после каждой записи
    print(f'Завершилась запись в файл {file_name}')  # Сообщение о завершении

# Вызов функции без потоков
time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f"Работа без потоков: {time_end - time_start} секунд")

# Создание потоков
time_start_threads = datetime.now()

# Создаем и запускаем потоки
threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

# Запуск всех потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

time_end_threads = datetime.now()

print(f"Работа потоков: {time_end_threads - time_start_threads} секунд")
