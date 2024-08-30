import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:  # Если не передано правильное количество сторон,
                                            # используем значение sides_count по умолчанию
            sides = [1] * self.sides_count
        self.__sides = list(sides)  # Используем список сторон, переданных в конструктор
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        self.__sides

    def __len__(self):
            return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)  # Вызов конструктора базового класса перед инициализацией __sides
        self.__sides = [1] * self.sides_count if len(sides) != self.sides_count else list(sides)

    def get_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def set_radius(self, new_radius):
        if isinstance(new_radius, (int, float)) and new_radius > 0:
            self.set_sides(new_radius * 2 * math.pi)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return int(self.get_sides()[0])  # Возвращает длину окружности

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != 3:
            raise ValueError("Треугольник должен иметь 3 стороны.")
        super().__init__(color, *sides)

    def get_square(self):
        s = sum(self.__sides) / 2
        return math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
    def get_volume(self):
       return self.__sides[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
