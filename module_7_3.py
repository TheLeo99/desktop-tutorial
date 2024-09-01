class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()  # Загружаем слова из файлов при инициализации

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip().lower()  # Переводим строку в нижний регистр и удаляем пробелы в начале и конце
                    for char in punctuation:
                        line = line.replace(char, ' ')  # Заменяем пунктуацию на пробелы
                    words = line.split()  # Разбиваем строку на слова
                    if file_name in all_words:
                        all_words[file_name].extend(words)  # Добавляем слова в существующий список
                    else:
                        all_words[file_name] = words  # Создаем новый список для файла

        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            word = word.lower()  # Приводим слово к нижнему регистру перед подсчётом
            if word in words:
                result[name] = words.index(word)
            else:
                result[name] = -1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            word = word.lower()  # Приводим слово к нижнему регистру перед подсчётом
            result[name] = words.count(word)
        return result

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего
