n = int(input())
ls = []
for i in range(n):
    nums = list(map(int, input().split()))
    ls.append(nums)
ps = []
for n1 in ls[0]:
    for n2 in ls[1]:
        p = (min(n1, n2), max(n1, n2))
        ps.append(p)
for i in range(2, n):
    nps = []
    for s, e in ps:
        for num in ls[i]:
            ns = min(s, num)
            ne = max(e, num)
            nps.append((ns, ne))
    ps = nps
mr = None
mins = 10e18
for s, e in ps:
    size = e - s
    f = True
    for lst in ls:
        hn = False
        for num in lst:
            if s <= num <= e:
                hn = True
                break
        if not hn:
            f = False
            break
    if f and size < mins:
        mins = size
        mr = (s, e)
print(f"{mr[0]}-{mr[1]}")
