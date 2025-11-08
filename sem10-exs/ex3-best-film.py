n = int(input())
v = {}
for i in range(n):
    f = input().strip()
    if f in v:
        v[f] += 1
    else:
        v[f] = 1
fs = []
for f, num in v.items():
    fs.append([f, num])
for i in  range(len(fs)):
    for j in range(i+1, len(fs)):
        if fs[i][1] < fs[j][1]:
            fs[i], fs[j] = fs[j], fs[i]
for f, num in fs:
    print(f, num)
