import random
import time
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Замок для синхронизации доступа к балансу
        self.deposit_count = 0  # Счетчик транзакций пополнения
        self.take_count = 0  # Счетчик транзакций снятия

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)

            with self.lock:  # Блокировка для безопасного доступа к балансу
                self.balance += amount
                self.deposit_count += 1
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

            time.sleep(0.1)  # Имитация задержки выполнения операции пополнения

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")

            with self.lock:  # Блокировка для безопасного доступа к балансу
                if amount <= self.balance:
                    # Когда баланс достаточный, снимаем средства
                    self.balance -= amount
                    self.take_count += 1
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")

            time.sleep(0.1)  # Задержка перед следующей транзакцией


# Создание объекта банка
bk = Bank()

# Создание потоков для пополнения и снятия средств
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f"Итоговый баланс: {bk.balance}")
