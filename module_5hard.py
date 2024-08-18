import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)  # хэширование пароля
        self.age = age

    def hash_password(self, password):
        # применяется sha256 (криптографическая хэш-функция)
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)  # преобразование в целое число


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0  # по умолчанию видео остановлено
        self.adult_mode = adult_mode  # по умолчанию ограничение по возрасту отключено

    def play(self):
        if self.time_now < self.duration:
            self.time_now = 0
        else:
            print(f"Видео '{self.title}' уже завершено.")

    def stop(self):
        self.time_now = 0

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == User.hash_password(user, password):
                self.current_user = user
                return True
        print(f"Неправильный логин или пароль для пользователя '{nickname}'.")
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        results = []
        for video in self.videos:
            if search_word in video.title.lower():
                results.append(video.title)
        return results

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                break  # Прерываем цикл, если видео найдено
        else:  # Этот блок выполняется, если цикл завершился без break
            video = None
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        video.play()
        for i in range(video.duration):
            i = i + 1
            print(i)
            time.sleep(1)
        video.stop()
        print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
