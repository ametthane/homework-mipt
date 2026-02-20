inp1 = input().split()
v = int(inp1[0])
e = int(inp1[1])
inp2 = input().strip()
inp2 = inp2.replace('{', '[').replace('}', ']')
adj = eval(inp2)
visited = [False] * v


def dfs(v, par):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            if dfs(u, v):
                return True
        elif u != par:
            return True
    return False


res = False
for i in range(v):
    if not visited[i]:
        if dfs(i, -1):
            res = True
            break
if res:
    print("YES")
else:
    print("NO")
