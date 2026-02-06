nums = list(map(int, input().split()))
m_fr = 0
ans = 0
for i in range(len(nums)):
    c = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            c += 1
    if c > m_fr:
        m_fr = c
        ans = nums[i]
print (ans)