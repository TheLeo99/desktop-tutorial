def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()  # при вызове inner_function внутри test_function функция работает


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")


inner_function()


test_function()  # NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
