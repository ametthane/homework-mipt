import math
inp = list(map(int, input().split()))
r = inp[0]
a = inp[1]
c = math.pi*r*2
per = ((math.pi*r*r)/(a**2))*100
print(f'Длина окружности равна {c:.2f}. Площадь круга составляет {per:.2f}% от площади квадрата')