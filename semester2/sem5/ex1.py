import math
n = int(input())
pts = []
for _ in range(n):
    x, y = map(int, input().split())
    pts.append((x, y))
used = [0] * n
INF = float('inf')
mind2 = [INF] * n
used[0] = 0
for i in range(1, n):
    dx = pts[0][0] - pts[i][0]
    dy = pts[0][1] - pts[i][1]
    mind2[i] = dx * dx + dy * dy
ans = 0.0
for _ in range(n - 1):
    v = -1
    best = INF
    for i in range(n):
        if not used[i] and mind2[i] < best:
            best = mind2[i]
            v = i
    used[v] = 1
    ans += math.sqrt(best)
    xv, yv = pts[v]
    for i in range(n):
        if not used[i]:
            dx = xv - pts[i][0]
            dy = yv - pts[i][1]
            d2 = dx * dx + dy * dy
            if d2 < mind2[i]:
                mind2[i] = d2
print(int(ans))
