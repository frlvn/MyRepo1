import abc
import math

class Figure(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

class Ellipse(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2) / 2)


circle = Circle(radius=5, x=0, y=0)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(width=10, height=5)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

triangle = Triangle(a=3, b=4, c=5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

ellipse = Ellipse(a=4, b=2)
print("Ellipse area:", ellipse.area())
print("Ellipse perimeter:", ellipse.perimeter())
input('Waiting...')

'''Был создан абстрактный базовый класс Figure с абстрактными методами area и perimeter. Далее, были созданы дочерние классы Circle, Rectangle, Triangle и Ellipse, которые наследуются от базового класса Figure и реализуют его абстрактные методы. Каждый из дочерних классов имеет свои свойства и методы, соответствующие конкретной геометрической фигуре. Например, в классе Circle были добавлены свойства radius, x и y для хранения радиуса и координат центра, а также методы для вычисления длины окружности и площади круга. Далее были созданы объекты каждого из классов Circle, Rectangle, Triangle и Ellipse, задавая им конкретные значения свойств. Затем мы вызываем методы area() и perimeter() для каждого объекта, чтобы вычислить площадь и периметр соответствующей фигуры и вывести полученные данные в консоль.'''
