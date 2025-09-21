import numpy as np

def solve(n, m, row):
    a = np.array(row, dtype=int)
    c = a[:, :-1]
    b = a[:, -1]
    return np.linalg.solve(c, b)


N, M = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(N)]
ans = solve(N, M, rows)
print(*ans)