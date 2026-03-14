import math
n = int(input().strip())
coords = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    coords.append((x, y))
dist = [[0.0] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        d = math.hypot(coords[i][0] - coords[j][0],
                       coords[i][1] - coords[j][1])
        dist[i][j] = d
        dist[j][i] = d
for k in range(n):
    for i in range(n):
        for j in range(n):
            thr = max(dist[i][k], dist[k][j])
            if thr < dist[i][j]:
                dist[i][j] = thr
ans = dist[0][1]
print(f'{ans:.3f}')
