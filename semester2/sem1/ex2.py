graph = {}
m = int(input())
while True:
    inp = input().strip().split()
    if not inp:  # ввести пустую строку в конце, чтоб закончить ввод пар узлов
        break
    u = int(inp[0])
    v = int(inp[1])
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
s, e = map(int, input().split())
visited = []
q = []
q.append(s)
visited.append(s)
f = 0
while q:
    cur = q[0]
    q = q[1:]
    if cur == e:
        f = 1
        break
    if cur in graph:
        for n in graph[cur]:
            if n not in visited:
                visited.append(n)
                q.append(n)
if f == 0:
    print('false')
else:
    print('true')
