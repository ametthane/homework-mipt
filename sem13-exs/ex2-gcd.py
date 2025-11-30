import math
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
s = 1
while s < n:
    s *= 2


def build_tree(a):
    tree = [0] * (2 * s)
    for i in range(n):
        tree[s + i] = a[i]
    for i in range(s - 1, 0, -1):
        tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])
    return tree


def query(tree, le, r):
    le += s - 1
    r += s - 1
    ans = 0
    while le <= r:
        if le % 2 == 1:
            ans = math.gcd(ans, tree[le])
            le += 1
        if r % 2 == 0:
            ans = math.gcd(ans, tree[r])
            r -= 1
        le = le // 2
        r = r // 2
    return ans


tr = build_tree(arr)
res = []
for i in range(k):
    le, r = map(int, input().split())
    res.append(query(tr, le, r))
print(" ".join(map(str, res)))
