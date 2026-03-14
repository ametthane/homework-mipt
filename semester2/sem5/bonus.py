pt = []
rank = []


def find(x):
    while pt[x] != x:
        pt[x] = pt[pt[x]]
        x = pt[x]
    return x


def union(x, y):
    xr = find(x)
    yr = find(y)
    if xr == yr:
        return False
    if rank[xr] < rank[yr]:
        pt[xr] = yr
    elif rank[xr] > rank[yr]:
        pt[yr] = xr
    else:
        pt[yr] = xr
        rank[xr] += 1
    return True


while True:
    inp = input()
    if not inp:
        continue
    parts = inp.split()
    cmd = parts[0]

    if cmd == "RESET":
        n = int(parts[1])
        pt = list(range(n))
        rank = [0] * n
        print("RESET DONE")

    elif cmd == "JOIN":
        j = int(parts[1])
        k = int(parts[2])
        if not union(j, k):
            print(f"ALREADY {j} {k}")

    elif cmd == "CHECK":
        j = int(parts[1])
        k = int(parts[2])
        if find(j) == find(k):
            print("YES")
        else:
            print("NO")