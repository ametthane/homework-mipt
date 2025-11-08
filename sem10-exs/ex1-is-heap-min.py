a = list(map(int, input().split()))
n = len(a)
f = 1
for i in range(n):
    le = 2 * i + 1
    ri = 2 * i + 2
    if le < n and a[le] < a[i]:
        f = 0
        break
    if ri < n and a[ri] < a[i]:
        f = 0
        break
print(f)
