with open('input.txt', 'r') as f:
    inp = f.read().strip().splitlines()
n = int(inp[0])
nm = inp[1].strip()
m = len(nm)
cbs = []
for i in range(2, len(inp)):
    cbs.append(inp[i].strip())
    if len(cbs) == n:
        break

if len(cbs) < n:
    with open('output.txt', 'w') as f:
        f.write('NO')
    exit()

adj = [[] for _ in range(m)]
for i, ch in enumerate(nm):
    for j, c in enumerate(cbs):
        if ch in c:
            adj[i].append(j)
mr = [-1] * n


def dfs(u, used):
    for v in adj[u]:
        if not used[v]:
            used[v] = 1
            if mr[v] == -1 or dfs(mr[v], used):
                mr[v] = u
                return 1
    return 0


res = 0
for u in range(m):
    used = [0] * n
    if dfs(u, used):
        res += 1
    else:
        break
if res == m:
    ans = [0] * m
    for v in range(m):
        if mr[v] != -1:
            ans[mr[v]] = v + 1
    with open('output.txt', 'w') as f:
        f.write('YES\n')
        f.write(' '.join(map(str, ans)))
else:
    with open('output.txt', 'w') as f:
        f.write('NO')
