nums = list(map(int, input().split()))
nums.insert(0, nums[len(nums)-1])
nums.pop(len(nums)-1)
print(" ".join(str(n) for n in nums))