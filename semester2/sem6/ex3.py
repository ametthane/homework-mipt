n = int(input("Количество вершин: "))
if n % 2 != 0:
    print(0)
else:
    c = 0
    used = [0] * n

    def dfs(ps):
        global c
        if ps == n // 2:
            c += 1
            return

        u = -1
        for i in range(n):
            if not used[i]:
                u = i
                break
        used[u] = 1
        for v in range(u + 1, n):
            if not used[v]:
                used[v] = 1
                dfs(ps + 1)
                used[v] = 0
        used[u] = 0

    dfs(0)
    print(c)  # для n = 6 ответ 15.
