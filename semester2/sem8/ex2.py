import math

r, a = map(int, input().split())
c = 2 * math.pi * r
s = math.pi * r * r
sq = a * a
print(f"Длина окружности равна {c:.2f}. "
      f"Площадь круга составляет {s/sq:.2f}% от площади квадрата.")
