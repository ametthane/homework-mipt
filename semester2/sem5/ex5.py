import heapq
inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
cs = inp[2:]
gr = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    gr[u].append((v, w))
    gr[v].append((u, w))
INF = float('inf')
dist = [INF] * n
pq = []

for c in cs:
    dist[c] = 0
    heapq.heappush(pq, (0, c))
while pq:
    d, v = heapq.heappop(pq)
    if d > dist[v]:
        continue
    for to, w in gr[v]:
        nd = d + w
        if nd < dist[to]:
            dist[to] = nd
            heapq.heappush(pq, (nd, to))
ans = 0
for i in range(n):
    if dist[i] != INF:
        ans += dist[i]

print(ans)
