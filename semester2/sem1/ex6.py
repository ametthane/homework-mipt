words = input().strip().split()
st = {}
en = {}
for w in words:
    first = w[0]
    last = w[-1]
    if first in st:
        st[first] += 1
    else:
        st[first] = 1
    if last in en:
        en[last] += 1
    else:
        en[last] = 1
ls = set()
for le in st:
    ls.add(le)
for le in en:
    ls.add(le)
ans = True
for le in ls:
    sts = st.get(le, 0)
    ens = en.get(le, 0)
    if sts != ens:
        ans = False
        break
print(ans)
