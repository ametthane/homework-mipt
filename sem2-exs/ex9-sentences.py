with open(r'input.txt', 'r') as inp:
    s = inp.read().strip()
ans = 0
i = 0
while i < len(s):
    if s[i] in '.!?':
        ans += 1
        while i < len(s) and s[i] in '.!?':
            i += 1
    else:
        i += 1
with open(r'output.txt', 'w') as outp:
    outp.write(str(ans))