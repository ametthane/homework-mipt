n = int(input())
sts = list(map(int, input().split()))
ens = list(map(int, input().split()))
ms = list(zip(sts, ens))
ms.sort(key=lambda x: x[1])
c = 0
le = -1
for s, e in ms:
    if s > le:
        c += 1
        le = e
print(c)
