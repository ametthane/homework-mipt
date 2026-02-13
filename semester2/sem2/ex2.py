from collections import deque


def solve(n, st_x, st_y):
    mvs = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (1, -2)
    ]
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((st_x, st_y))
    dist[st_x][st_y] = 0
    while queue:
        x, y = queue.popleft()
        curr_dist = dist[x][y]
        for dx, dy in mvs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = curr_dist + 1
                queue.append((nx, ny))
    return dist


n = 8
st_x = 0
st_y = 0
res = solve(n, st_x, st_y)
for r in res:
    print(' '.join(f'{c}' for c in r))
