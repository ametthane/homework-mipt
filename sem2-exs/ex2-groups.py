nstr = list(input().split(" "))
n = int(nstr[0])
s = nstr[1]
rev = []
for i in range(0, len(s), n):
    g = s[i:i+n]
    rev.append(g[::-1])
print("".join(rev))