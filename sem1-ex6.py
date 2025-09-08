def to_dec(num, base):
    return int(num, base)


def to_any_base (num, base):
    if num == 0:
        return "0"
    dig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while num > 0:
        res = dig[num % base] + res
        num //= base
    return res


with open(r'input.txt', 'r') as inp:
    nums_inp = inp.readline().strip().split()
    op = inp.readline().strip()
    base = int(inp.readline().strip())

nums = [to_dec(n, base) for n in nums_inp]
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
ans = to_any_base(ans, base)

with open(r'output.txt', 'w') as outp:
    outp.write(str(ans))