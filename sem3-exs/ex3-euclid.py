def euc_extended(a, b):
    if a == 0:
        return 0, 1, b
    else:
        x1, y1, gcd = euc_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
    return x, y, gcd


ab = list(map(int, input().split()))
a = ab[0]
b = ab[1]
x0, y0, d = euc_extended(a, b)
if b % d == 0 and a % d == 0:
    x = x0 - 1*(b/d)
    y = y0 + 1*(a/d)
else:
    x = x0 - b
    y = y0 + a
if abs(x0) + abs(y0) > abs(x) + abs(y):
    print(int(x), int(y), d)
elif abs(x0) + abs(y0) == abs(x) + abs(y):
    if x < x0:
        print(int(x), int(y), d)
    else:
        print(x0, y0, d)
else:
    print(x0, y0, d)