def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов
    for func in functions:  # Перебираем все переданные функции
        try:
            # Проверяем, что функция имеет атрибут __name__, иначе пропускаем её
            if hasattr(func, '__name__'):
                func_name = func.__name__  # Получаем имя функции
                results[func_name] = func(int_list)  # Применяем функцию и записываем результат
            else:
                raise ValueError(f"Объект {func} не является допустимой функцией")
        except Exception as e:
            # В случае ошибки записываем сообщение об ошибке
            results[func.__name__] = f"Ошибка: {str(e)}"
    return results  # Возвращаем словарь с результатами


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
