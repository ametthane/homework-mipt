graph = {}
m = int(input())
for i in range(m-1):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
visited = []
q = []
v0 = list(graph.keys())[0]
q.append(v0)
visited.append(v0)
while q:
    cur = q[0]
    q = q[1:]
    if cur in graph:
        for n in graph[cur]:
            if n not in visited:
                visited.append(n)
                q.append(n)
if len(graph) == 0:
    print('True')
elif len(visited) == len(graph):
    print('True')
else:
    print('False')
