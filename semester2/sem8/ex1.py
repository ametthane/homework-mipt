s = input()
ns = []
sc = []
i = 0
while i < len(s):
    if s[i:i+8] == "student_":
        num = s[i+8:i+11]
        i += 11
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        score = int(s[i:j])
        ns.append(num)
        sc.append(score)
        i = j
    else:
        i += 1
m = max(sc)
res = [ns[k] for k in range(len(ns)) if sc[k] == m]
print('-'.join(res))
