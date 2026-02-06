edg = []
while True:
    inp = input().strip()
    if not inp:
        break
    u, v, w = map(int, inp.split())
    edg.append((u, v, w))
st, en = map(int, input().split())
vs1 = set()
for u, v, w in edg:
    vs1.add(u)
    vs1.add(v)
vs = sorted(list(vs1))
INF = 10**9
dist = {}
for v in vs:
    dist[v] = INF
dist[st] = 0
gr = {}
for v in vs:
    gr[v] = []
for u, v, w in edg:
    gr[u].append((v, w))
ch = [st]
while ch:
    cur = ch.pop(0)
    for nei, wei in gr[cur]:
        newdist = dist[cur] + wei
        if newdist < dist[nei]:
            dist[nei] = newdist
            if nei not in ch:
                ch.append(nei)
print(dist[en])
