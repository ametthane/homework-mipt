def find_clusters(n, rel):
    gr: list[list[int]] = [[] for _ in range(n)]
    for a, b in rel:
        gr[a].append(b)
    visited = [False] * n
    st = []

    def dfs1(v: int):
        visited[v] = True
        for t in gr[v]:
            if not visited[t]:
                dfs1(t)
        st.append(v)

    for i in range(n):
        if not visited[i]:
            dfs1(i)
    rev_gr = [[] for _ in range(n)]
    for a in range(n):
        for b in gr[a]:
            rev_gr[b].append(a)
    visited = [False] * n

    def dfs2(v: int, comp):
        visited[v] = True
        comp.append(v)
        for t in rev_gr[v]:
            if not visited[t]:
                dfs2(t, comp)

    cl = []
    while st:
        v = st.pop()
        if not visited[v]:
            comp = []
            dfs2(v, comp)
            comp.sort()
            cl.append(comp)
    cl.sort(key=lambda c: len(c), reverse=True)
    return cl


rel = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 3)]
res = find_clusters(4, rel)
print(res)
