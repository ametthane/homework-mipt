n = int(input())
m = int(input())
gr = [[] for i in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    gr[u].append(v)
    gr[v].append(u)
visited = [False] * n


def dfs(v):
    visited[v] = True
    for nb in gr[v]:
        if not visited[nb]:
            dfs(nb)


cms = 0
for v in range(n):
    if not visited[v]:
        dfs(v)
        cms += 1
print(cms)
