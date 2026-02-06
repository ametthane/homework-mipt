def dfs(v, prev, visited, gr):
    visited[v] = True
    if v in gr:
        ws = gr[v]
    else:
        ws = []
    for w in ws:
        if w not in visited:
            if dfs(w, v, visited, gr):
                return True
        elif w != prev:
            return True
    return False


n = int(input())
gr = {}
while True:
    inp = input().strip()
    if not inp:
        break
    u, v = map(int, inp.split())
    if u not in gr:
        gr[u] = []
    gr[u].append(v)
    if v not in gr:
        gr[v] = []
    gr[v].append(u)
visited = {}
ans = False
for ver in gr:
    if ver not in visited:
        if dfs(ver, None, visited, gr):
            ans = True
            break
print(ans)
