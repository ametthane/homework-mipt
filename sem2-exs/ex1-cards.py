nums = list(map(int, input().split()))
s = (nums[0]*(nums[0]+1))/2
ss = sum(nums)-nums[0]
print(s)
print(s-ss)

