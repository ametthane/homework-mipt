n = int(input())
nums = list(map(int, input().split()))
s = sum(nums)
print(f'{(s / n):.0f}')