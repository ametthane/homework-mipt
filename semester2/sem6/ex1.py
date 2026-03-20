with open('input.txt', 'r') as f:
    inp = f.read().strip().split()
n = int(inp[0])
m = int(inp[1])
es = []
idx = 2
for _ in range(m):
    u = int(inp[idx]) - 1
    v = int(inp[idx + 1]) - 1
    idx += 2
    es.append((u, v))
adj = [[] for _ in range(n)]
for u, v in es:
    adj[u].append(v)
    adj[v].append(u)
c = [-1] * n
check = 1
for st in range(n):
    if c[st] == -1:
        c[st] = 0
        q = [st]
        while q:
            u = q.pop()
            for v in adj[u]:
                if c[v] == -1:
                    c[v] = c[u] ^ 1
                    q.append(v)
                elif c[v] == c[u]:
                    check = 0
                    break
            if not check:
                break
    if not check:
        break
with open('output.txt', 'w') as f:
    f.write('YES' if check else 'NO')
