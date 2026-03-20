with open('input.txt', 'r') as f:
    inp = f.read().strip().splitlines()
n = int(inp[0])
a = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, inp[i].split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]
u = [0] * (n + 1)
v = [0] * (n + 1)
p = [0] * (n + 1)
way = [0] * (n + 1)
for i in range(1, n + 1):
    p[0] = i
    j0 = 0
    minv = [float('inf')] * (n + 1)
    used = [0] * (n + 1)
    while True:
        used[j0] = 1
        i0 = p[j0]
        delta = float('inf')
        j1 = 0
        for j in range(1, n + 1):
            if not used[j]:
                cur = a[i0][j] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
        for j in range(0, n + 1):
            if used[j]:
                u[p[j]] += delta
                v[j] -= delta
            else:
                minv[j] -= delta
        j0 = j1
        if p[j0] == 0:
            break
    while True:
        j1 = way[j0]
        p[j0] = p[j1]
        j0 = j1
        if j0 == 0:
            break
ans = 0
for j in range(1, n + 1):
    ans += a[p[j]][j]
with open('output.txt', 'w') as f:
    f.write(str(ans))
