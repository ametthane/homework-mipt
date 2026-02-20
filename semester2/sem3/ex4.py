inp1 = input().split()
vv = int(inp1[0])
ee = int(inp1[1])
stn = inp1[2]
enn = inp1[3]
ntoi = {}
ns = []
gr = [[] for _ in range(vv)]

for _ in range(ee):
    eg = input().split()
    un = eg[0]
    vn = eg[1]
    w = int(eg[2])
    if un not in ntoi:
        ntoi[un] = len(ns)
        ns.append(un)
    if vn not in ntoi:
        ntoi[vn] = len(ns)
        ns.append(vn)
    u = ntoi[un]
    v = ntoi[vn]
    gr[u].append((v, w))
    gr[v].append((u, w))
st = ntoi[stn]
en = ntoi[enn]
INF = float('inf')
dist = [INF] * vv
par = [-1] * vv
visited = [False] * vv
dist[st] = 0
for _ in range(vv):
    u = -1
    mind = INF
    for i in range(vv):
        if not visited[i] and dist[i] < mind:
            mind = dist[i]
            u = i
    if u == -1:
        break
    visited[u] = True
    for v, w in gr[u]:
        if not visited[v] and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            par[v] = u
print(dist[en])
pathi = []
cur = en
while cur != -1:
    pathi.append(cur)
    cur = par[cur]
pathi.reverse()
pathn = [ns[i] for i in pathi]
with open('paths.txt', 'w') as f:
    for n in pathn:
        f.write(n + '\n')
print(' --> '.join(pathn))
