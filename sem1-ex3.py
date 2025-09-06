import math
l = list(map(int, input("Введите числа через пробел: ").split()))
prod = 1
for i in range(len(l)):
    prod *= l[i]
print("Среднее геометрическое чисел: ", round(math.sqrt(prod), 2))