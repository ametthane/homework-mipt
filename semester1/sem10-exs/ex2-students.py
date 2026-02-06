fr = list(map(int, input().split()))
sw = list(map(int, input().split()))
pia = list(map(int, input().split()))
res = []
for num in sw:
    if num in pia and num not in fr:
        res.append(num)
print(*res)
