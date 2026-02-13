def minimax(gr, st):
    n = len(gr)
    INF = float('inf')
    d = [INF] * n
    visited = [False] * n
    d[st] = 0
    for _ in range(n):
        u = -1
        best = INF
        for i in range(n):
            if not visited[i] and d[i] < best:
                best = d[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in gr[u]:
            nmax = max(d[u], w)
            if nmax < d[v]:
                d[v] = nmax
    return d


def product(gr, st):
    n = len(gr)
    INF = float('inf')
    d = [INF] * n
    visited = [False] * n
    d[st] = 1
    for _ in range(n):
        u = -1
        best = INF
        for i in range(n):
            if not visited[i] and d[i] < best:
                best = d[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in gr[u]:
            nprod = d[u] * w
            if nprod < d[v]:
                d[v] = nprod
    return d


def maximin(gr, st):
    n = len(gr)
    INF = float('inf')
    d = [-INF] * n
    visited = [False] * n
    d[st] = INF
    for _ in range(n):
        u = -1
        best = -INF
        for i in range(n):
            if not visited[i] and d[i] > best:
                best = d[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in gr[u]:
            nmin = min(d[u], w)
            if nmin > d[v]:
                d[v] = nmin
    return d


def colour(gr, cols, st):
    n = len(gr)
    INF = float('inf')
    chs = [INF] * n
    lens = [INF] * n
    visited = [False] * n
    chs[st] = 0
    lens[st] = 0
    for _ in range(n):
        u = -1
        best_c = INF
        best_l = INF
        for i in range(n):
            if not visited[i]:
                if (chs[i], lens[i]) < (best_c, best_l):
                    best_c = chs[i]
                    best_l = lens[i]
                    u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in gr[u]:
            if cols[v] == cols[u]:
                nc = chs[u]
            else:
                nc = chs[u] + 1
            nl = lens[u] + w
            if (nc, nl) < (chs[v], lens[v]):
                chs[v] = nc
                lens[v] = nl
    return chs, lens


gr = [
    [(1, 5), (2, 3)],
    [(2, 2), (3, 6)],
    [(3, 7)], []
]
st = 0
d1 = minimax(gr, st)
for i in range(len(d1)):
    print(f'd[{i}] = {d1[i]}')
print('\n')
d2 = product(gr, st)
for i in range(len(d2)):
    print(f'd[{i}] = {d2[i]}')
print('\n')
d3 = maximin(gr, st)
for i in range(len(d3)):
    print(f'd[{i}] = {d3[i]}')
print('\n')
cols = [1, 2, 1, 2]
chs, lens = colour(gr, cols, st)
for i in range(len(gr)):
    print(f'вершина {i}: смена цвета = {chs[i]}, длина = {lens[i]}')
