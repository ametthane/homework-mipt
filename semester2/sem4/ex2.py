c = int(input().strip())
ans = []
for _ in range(c):
    ln = input().strip()
    while ln == '':
        ln = input().strip()
    n, m = map(int, ln.split())
    es = []
    for _ in range(m):
        x, y, t = map(int, input().split())
        es.append([x, y, t])
    INF = 10**9
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n - 1):
        upd = False
        for (u, v, w) in es:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                upd = True
        if not upd:
            break
    neg = False
    for (u, v, w) in es:
        if dist[u] != INF and dist[u] + w < dist[v]:
            neg = True
            break
    ans.append('Возможно' if neg else 'не возможно')
print('\n'.join(ans))
