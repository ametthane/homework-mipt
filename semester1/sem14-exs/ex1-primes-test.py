import math


def isprime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def decompose(x, i=2):
    if x == 1:
        return []
    if isprime(i) is True and x % i == 0:
        return [i] + decompose(x//i, i)
    return decompose(x, i+1)


for num in range(2, 101):
    fs = decompose(num)
    pr = 1
    for fr in fs:
        pr *= fr
    assert pr == num, (f"Ошибка для {num}:"
                       f" произведение {fs} = {pr}, а должно быть {num}")
for num in range(2, 101):
    fs = decompose(num)
    for fr in fs:
        assert isprime(fr), (f"Ошибка для {num}:"
                             f" множитель {fr} не является простым числом")
for num in range(2, 101):
    fs = decompose(num)
    for i in range(len(fs) - 1):
        assert fs[i] <= fs[i + 1], (f"Ошибка для {num}:"
                                    f" множители не отсортированы {fs}")
n = int(input())
print(" * ".join(map(str, decompose(n))))
