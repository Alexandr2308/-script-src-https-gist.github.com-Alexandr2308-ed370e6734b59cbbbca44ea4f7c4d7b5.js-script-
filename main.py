# Задание 1
# Создать базовый класс Фигура с методом для подсчета площади.
# Создать производные классы: прямоугольник, круг, прямоугольный треугольник,
# трапеция со своими методами для подсчета площади.
# Задание 2
# Для классов из задания 1 нужно переопределить маги- ческие методы int(возвращает площадь) и
# str (возвращает информацию о фигуре).
class Figura:
    def __init__(self):
        self.b = None
        self.a = None
        self.r = None

    def area_rectangle(self):
        return self.a * self.b

    def area_circle(self):
        return 3.14 * self.r ** 2

    def area_triangle(self):
        return (self.a * self.b) / 2

    def area_parallelogram(self):
        return self.a * self.b


class Rectangle(Figura):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def __str__(self):
        return f'Area rectangle: a={self.a} b={self.b} S={self.area_rectangle()}'

    def __int__(self):
        return self.area_rectangle()


class Circle(Figura):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def __str__(self):
        return f'Area circle: r={self.r} S={self.area_circle()}'

    def __int__(self):
        return self.area_circle()


class Triangle(Figura):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def __str__(self):
        return f'Area triangle: a={self.a} b={self.b} S={self.area_triangle()}'

    def __int__(self):
        return self.area_triangle()


class Parallelogram(Figura):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def __str__(self):
        return f'Area parallelogram: a={self.a} b={self.b} S={self.area_parallelogram()}'

    def __int__(self):
        return self.area_parallelogram()


a = Rectangle(5, 4)
b = Circle(5)
c = Triangle(5, 6)
d = Parallelogram(5, 10)

print(a.__str__())
print(type(a.__str__()))
print(a.__int__())
print(type(a.__int__()))
print(b.__str__())
print(b.__int__())
print(c.__str__())
print(c.__int__())
print(d.__str__())
print(d.__int__())
