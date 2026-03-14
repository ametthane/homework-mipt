n, m = map(int, input().split())
eds = []
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    eds.append((u, v, w, i))
pt = list(range(n))
rank = [0] * n


def find(x):
    while pt[x] != x:
        pt[x] = pt[pt[x]]
        x = pt[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if rank[x] < rank[y]:
        pt[x] = y
    elif rank[x] > rank[y]:
        pt[y] = x
    else:
        pt[y] = x
        rank[x] += 1
    return True


seds = sorted(eds, key=lambda e: e[2])
mstw = 0
in_mst = [False] * m
mst_adj = [[] for _ in range(n)]
for u, v, w, idx in seds:
    if union(u, v):
        mstw += w
        in_mst[idx] = True
        mst_adj[u].append((v, w))
        mst_adj[v].append((u, w))


def max_edge_on_path(u, v):
    pt = [-1] * n
    st = [(u, -1, 0)]
    pt[u] = u
    while st:
        cur, par, w_par = st.pop()
        if cur == v:
            break
        for nxt, w in mst_adj[cur]:
            if nxt != par:
                pt[nxt] = cur
                st.append((nxt, cur, w))
    max_w = 0
    cur = v
    while cur != u:
        for nxt, w in mst_adj[cur]:
            if nxt == pt[cur]:
                max_w = max(max_w, w)
                break
        cur = pt[cur]
    return max_w


ans = [0] * m
for u, v, w, idx in eds:
    if in_mst[idx]:
        ans[idx] = mstw
    else:
        mx = max_edge_on_path(u, v)
        ans[idx] = mstw + w - mx
print('\n'.join(map(str, ans)))
