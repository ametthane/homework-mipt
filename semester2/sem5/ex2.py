n = int(input())
ws = input().split()
M, L = map(int, input().split())
board = []
for _ in range(M):
    board.append(input().split())
wset = set(ws)
prefs = set()
for w in ws:
    for i in range(1, len(w) + 1):
        prefs.add(w[:i])
ds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
found = set()


def dfs(i, j, cur, vis):
    cur += board[i][j]
    if cur in wset:
        found.add(cur)
    if cur not in prefs:
        return
    vis.add((i, j))
    for di, dj in ds:
        ni, nj = i + di, j + dj
        if 0 <= ni < M and 0 <= nj < L and (ni, nj) not in vis:
            dfs(ni, nj, cur, vis)
    vis.remove((i, j))


for i in range(M):
    for j in range(L):
        dfs(i, j, '', set())
print(' '.join(sorted(found)))
