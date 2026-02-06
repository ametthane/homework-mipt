inp = input().split()
flights = {}
for i in range(0, len(inp), 2):
    s = inp[i]
    e = inp[i + 1]
    flights[s] = e
al = set(flights.values())
start = None
for a in flights.keys():
    if a not in al:
        start = a
        break
route = []
cur = start
while cur is not None:
    route.append(cur)
    cur = flights.get(cur)
print(route)
