import math
class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            x, y, z = x.strip('() {}').replace(' ', '').split(',')
        x = float(x)
        y = float(y)
        z = float(z)
        assert isinstance(x, (int, float)), "x должен быть числом"
        assert isinstance(y, (int, float)), "y должен быть числом"
        assert isinstance(z, (int, float)), "z должен быть числом"
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return self.x * other.x, self.y * other.y, self.z * other.z
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


def mass_center(vectors):
    n = len(vectors)
    sum_x = sum(v.x for v in vectors)
    sum_y = sum(v.y for v in vectors)
    sum_z = sum(v.z for v in vectors)
    return Vector(round(sum_x / n), round(sum_y / n), round(sum_z / n))


def triangle_area(a, b, c):
    ab = b - a
    ac = c - a
    return 0.5 * abs((ab.y*ac.z - ab.z*ac.y) - (ab.x*ac.z - ab.z*ac.x) + (ab.x*ac.y - ab.y*ac.x))


def max_area(vectors):
    n = len(vectors)
    max_a = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                area = triangle_area(vectors[i], vectors[j], vectors[k])
                if area > max_a:
                    max_a = area
    return max_a


c1 = input('Введите координаты первого вектора в скобках через запятую: ')
c2 = input('Введите координаты второго вектора в скобках через запятую: ')
v1 = Vector(c1)
v2 = Vector(c2)
print(f'Модуль первого вектора: {abs(v1):.2f},  модуль второго вектора: {abs(v2):.2f}')
print(f'Сложение: {v1+v2}')
print(f'Вычитание: {v1-v2}')
print(f'Скалярное произведение: {v1*v2}')
num = int(input('Введите число: '))
print(f'Умножение первого вектора на число: {v1*num}, умножение второго вектора на число: {v2*num}')

amount = int(input('Введите количество векторов, которые хотите добавить к первым двум: '))
vectors = [v1, v2]
for i in range(amount):
    c = input('Введите координаты вектора: ')
    v = Vector(c)
    vectors.append(v)

print(f'Центр масс точек: {mass_center(vectors)}')
print(f'Максимальная площадь треугольника: {max_area(vectors):.1f}')