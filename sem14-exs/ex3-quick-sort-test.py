def qs(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    le = []
    mid = []
    ri = []
    for x in a:
        if x < p:
            le.append(x)
        elif x > p:
            ri.append(x)
        else:
            mid.append(x)
    return qs(le) + mid + qs(ri)


def tests():
    assert qs([]) == []
    assert qs([7]) == [7]
    assert qs([1, 2, 3]) == [1, 2, 3]
    assert qs([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    t = [3, 1, 4, 1, 5, 9, 2]
    assert qs(t) == [1, 1, 2, 3, 4, 5, 9]
    assert qs([-5, -1, -3]) == [-5, -3, -1]
    assert qs([2, 2, 2]) == [2, 2, 2]
    b = list(range(50, 0, -1))
    assert qs(b) == list(range(1, 51))
    print("Все тесты пройдены успешно!")


s = input("Введите числа через пробел: ").split()
for x in s:
    assert x.isdigit() or (x[0] == '-' and x[1:].isdigit()), \
        f"Ошибка: '{x}' - не целое число"
num = []
for x in s:
    if x.isdigit():
        num.append(int(x))
    else:
        num.append(int(x))
print("До:", num)
res = qs(num)
print("После:", res)
print("\nЗапуск тестов...")
tests()
