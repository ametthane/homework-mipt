t = int(input())
for _ in range(t):
    line = input().strip()
    while line == '':
        line = input().strip()
    n = int(line)
    cnt = [0] * n
    for _ in range(n):
        a = int(input().strip())
        cnt[a - 1] += 1
    line = input().strip()
    while line == '':
        line = input().strip()
    e = int(line)
    swaps = []
    for _ in range(e):
        x, y = map(int, input().split())
        swaps.append((x - 1, y - 1))
    V = n + 2
    s = n
    tsink = n + 1
    INFcap = n
    g = [[] for _ in range(V)]

    def add_edge(fr, to, cap, cost):
        g[fr].append([to, len(g[to]), cap, cost])
        g[to].append([fr, len(g[fr]) - 1, 0, -cost])

    for x, y in swaps:
        add_edge(x, y, INFcap, 1)
        add_edge(y, x, INFcap, 1)
    ttl_flow = 0
    for i in range(n):
        if cnt[i] > 1:
            ex = cnt[i] - 1
            add_edge(s, i, ex, 0)
            ttl_flow += ex
        elif cnt[i] < 1:
            de = 1 - cnt[i]
            add_edge(i, tsink, de, 0)
    N = V
    h = [0] * N
    prevv = [0] * N
    preve = [0] * N
    res = 0
    flow = 0
    INF = 10 ** 9
    while flow < ttl_flow:
        dist = [INF] * N
        dist[s] = 0
        used = [False] * N
        while True:
            v = -1
            for u in range(N):
                if not used[u] and (v == -1 or dist[u] < dist[v]):
                    v = u
            if v == -1:
                break
            used[v] = True
            for i, e in enumerate(g[v]):
                if e[2] > 0:
                    nd = dist[v] + e[3] + h[v] - h[e[0]]
                    if dist[e[0]] > nd:
                        dist[e[0]] = nd
                        prevv[e[0]] = v
                        preve[e[0]] = i
        if dist[tsink] == INF:
            break
        for v in range(N):
            if dist[v] < INF:
                h[v] += dist[v]
        d = ttl_flow - flow
        v = tsink
        while v != s:
            e = g[prevv[v]][preve[v]]
            d = min(d, e[2])
            v = prevv[v]
        flow += d
        res += d * h[tsink]
        v = tsink
        while v != s:
            e = g[prevv[v]][preve[v]]
            e[2] -= d
            g[v][e[1]][2] += d
            v = prevv[v]
    print(res)
# Особая благодарность Deepseek за помощь в решении
