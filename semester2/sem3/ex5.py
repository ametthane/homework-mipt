from collections import deque
n, m = map(int, input().split())
gr = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)
    gr[v].append(u)
dist = [-1] * n
dist[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for v in gr[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
for d in dist:
    print(d)
