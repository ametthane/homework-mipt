nums = list(map(int, input().split()))
res = set()
for i in range(len(nums)):
    c = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            c += 1
    if c == 1:
        res.add(nums[i])
print (" ".join(str(n) for n in res))