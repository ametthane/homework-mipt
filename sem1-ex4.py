with open(r'input.txt', 'r') as inp:
    nums = list(map(int, inp.readline().split()))
    op = inp.readline().strip()

ans = nums[0]
if op == '+':
    for i in range(1, len(nums)):
        ans += nums[i]
elif op == '-':
    for i in range(1, len(nums)):
        ans -= nums[i]
elif op == '*':
    for i in range(1, len(nums)):
        ans *= nums[i]
with open(r'output.txt', 'w') as outp:
    outp.write(str(ans))