from collections import deque

n = int(input())
sts = list(map(int, input().split()))
ens = list(map(int, input().split()))
gr = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ens[i] < sts[j]:
            gr[i].append(j)
indeg = [0] * n
for i in range(n):
    for j in gr[i]:
        indeg[j] += 1
q = deque([i for i in range(n) if indeg[i] == 0])
topo = []
while q:
    u = q.popleft()
    topo.append(u)
    for v in gr[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
dp = [1] * n
for u in topo:
    for v in gr[u]:
        if dp[u] + 1 > dp[v]:
            dp[v] = dp[u] + 1
res = max(dp)
print(res)
