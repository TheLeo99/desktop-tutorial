def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # функция работает без ввода аргументов
print_params(b=25)  # функция работает c заменой значения и типа аргумента и без указания параметров по умолчанию
print_params(c=[1, 2, 3])  # функция работает c заменой значения и типа аргумента и без указания параметров по умолчанию

values_list = [178, 15.2, False]
values_dict = {'a': 'word', 'b': 169, 'c': [0, 1]}


print_params(*values_list)
print_params(**values_dict)

values_list_2 = [0, False]


print_params(*values_list_2, 42)
