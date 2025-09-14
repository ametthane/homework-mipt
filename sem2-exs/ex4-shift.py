nums = list(map(int, input().split()))
for i in range(0, len(nums)-1, 2):
    nums[i], nums[i+1] = nums[i+1], nums[i]
print(" ".join(str(n) for n in nums))