n, m, s, f = map(int, input().split())
gr = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    gr[u].append((v, w))
    gr[v].append((u, w))
INF = float('inf')
dist = [INF] * n
dist[s] = 0
parent = [-1] * n
visited = [False] * n
for _ in range(n):
    u = -1
    mind = INF
    for i in range(n):
        if not visited[i] and dist[i] < mind:
            mind = dist[i]
            u = i
    if u == -1:
        break
    visited[u] = True
    for v, w in gr[u]:
        if not visited[v] and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
path = []
cur = f
while cur != -1:
    path.append(cur)
    cur = parent[cur]
path.reverse()
print(len(path))
