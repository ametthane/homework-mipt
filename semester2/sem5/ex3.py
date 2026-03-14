import time
import heapq


def prim(g, n):
    used = [False] * n
    min_e = [float('inf')] * n
    min_e[0] = 0
    h = [(0, 0)]
    total = 0
    cnt = 0
    while h and cnt < n:
        w, v = heapq.heappop(h)
        if used[v]:
            continue
        used[v] = True
        total += w
        cnt += 1
        for to, w2 in g[v]:
            if not used[to] and w2 < min_e[to]:
                min_e[to] = w2
                heapq.heappush(h, (w2, to))
    return total


class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.r[x] < self.r[y]:
            self.p[x] = y
        elif self.r[x] > self.r[y]:
            self.p[y] = x
        else:
            self.p[y] = x
            self.r[x] += 1
        return True


def kruskal(e, n):
    e.sort(key=lambda x: x[2])
    dsu = DSU(n)
    total = 0
    cnt = 0
    for u, v, w in e:
        if dsu.union(u, v):
            total += w
            cnt += 1
            if cnt == n - 1:
                break
    return total


tests = [
    ("2 вершины, 1 ребро", 2, [(0, 1, 10)]),
    ("3 вершины, полный граф", 3, [(0, 1, 1), (0, 2, 2), (1, 2, 3)]),
    ("4 вершины, цепочка", 4, [(0, 1, 5), (1, 2, 7), (2, 3, 9)]),
    ("4 вершины, дерево + лишнее", 4, [(0, 1, 4), (1, 2, 2),
                                       (2, 3, 3), (0, 3, 10)]),
    ("5 вершин, небольшой граф", 5, [(0, 1, 6), (0, 2, 1), (1, 2, 2),
                                     (1, 3, 5), (2, 3, 3), (2, 4, 4),
                                     (3, 4, 8)]),
    ("6 вершин, разреженный", 6, [(0, 1, 2), (1, 2, 3), (2, 3, 4),
                                  (3, 4, 5), (4, 5, 6), (0, 5, 7)]),
    ("7 вершин, плотный", 7, [(i, j, (i + j) % 10 + 1)
                              for i in range(7) for j in range(i + 1, 7)]),
    ("8 вершин, случайный", 8, [(0, 1, 8), (0, 2, 5), (1, 2, 9),
                                (1, 3, 2), (2, 4, 7), (3, 4, 1), (3, 5, 4),
                                (4, 6, 3), (5, 7, 6), (6, 7, 2)]),
    ("9 вершин, средний", 9, [(0, 1, 3), (0, 2, 4), (1, 3, 5), (2, 4, 6),
                              (3, 5, 7), (4, 6, 8), (5, 7, 9),
                              (6, 8, 1), (7, 8, 2), (1, 4, 10)]),
    ("10 вершин, полный", 10, [(i, j, (i * j) % 20 + 1)
                               for i in range(10) for j in range(i + 1, 10)]),
]
print(f"{'Тест':<30} {'Прим (сек)':<15} {'Краскал (сек)':<15}")
for desc, n, e in tests:
    g = [[] for _ in range(n)]
    for u, v, w in e:
        g[u].append((v, w))
        g[v].append((u, w))
    st = time.perf_counter()
    w_prim = prim(g, n)
    t_prim = time.perf_counter() - st
    e_copy = e[:]
    st = time.perf_counter()
    w_krus = kruskal(e_copy, n)
    t_krus = time.perf_counter() - st
    print(f"{desc:<30} {t_prim:<15.7f} {t_krus:<15.7f}")
# Особая благодарность Deepseek за помощь с библиотекой time и написанием тестов
