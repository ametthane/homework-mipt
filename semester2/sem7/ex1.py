def mf(n, s, t, e):
    cap = [[0] * n for _ in range(n)]
    for u, v, b in e:
        u -= 1
        v -= 1
        cap[u][v] += b
        cap[v][u] += b
    par = [-1]*n
    ttl = 0
    while True:
        q = [s]
        par = [-1]*n
        par[s] = s
        while q:
            u = q.pop(0)
            if u == t:
                break
            for v in range(n):
                if par[v] == -1 and cap[u][v] > 0:
                    par[v] = u
                    q.append(v)
        if par[t] == -1:
            break
        aug = float('inf')
        v = t
        while v != s:
            u = par[v]
            aug = min(aug, cap[u][v])
            v = u
        v = t
        while v != s:
            u = par[v]
            cap[u][v] -= aug
            cap[v][u] += aug
            v = u
        ttl += aug
    return ttl


net_num = 1
while True:
    line = input().strip()
    while line == '':
        line = input().strip()
    n = int(line)
    if n == 0:
        break

    line = input().strip()
    while line == '':
        line = input().strip()
    s, t, c = map(int, line.split())

    es = []
    for _ in range(c):
        line = input().strip()
        while line == '':
            line = input().strip()
        u, v, bw = map(int, line.split())
        es.append((u, v, bw))

    ans = mf(n, s-1, t-1, es)

    print(f"Network {net_num}")
    print(f"The bandwidth is {ans}.")
    net_num += 1
