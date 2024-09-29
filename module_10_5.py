from multiprocessing import Pool
import time

def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        while True:
            line = file.readline()  # Считываем строку
            if not line:  # Если строка пустая, прерываем цикл
                break
            all_data.append(line.strip())  # Добавляем строку в список без лишних символов


filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Список названий файлов

"""
# Линейный вызов функции
start_time1 = time.time()

for name in filenames:
    data = read_info(name)  # Вызов функции

end_time1 = time.time()

print(f"Время выполнения при линейном вызове функции: {end_time1 - start_time1:.6f} секунд")
"""

# Многопроцессный вызов функции
if __name__ == '__main__':
    start_time2 = time.time()

    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_time2 = time.time()

    print(f"Время выполнения при многопроцессном вызове функции: {end_time2 - start_time2:.6f} секунд")
