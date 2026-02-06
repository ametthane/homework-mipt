n = int(input())
arr = list(map(int, input().split()))
m = int(input())
s = 1
while s < n:
    s *= 2


def build_tree(a):
    tree = [0] * (2 * s)
    for i in range(n):
        if a[i] == 0:
            tree[s + i] = 1
        else:
            tree[s + i] = 0
    for i in range(s - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree


def sum_tree(tree, le, r):
    _sum = 0
    le += s - 1
    r += s - 1
    while le <= r:
        if le % 2 == 1:
            _sum += tree[le]
            le += 1
        if r % 2 == 0:
            _sum += tree[r]
            r -= 1
        le = le // 2
        r = r // 2
    return _sum


def find_kth(tree, le, r, k):
    lef = le
    ri = r
    while lef <= ri:
        mid = (lef + ri) // 2
        c = sum_tree(tree, le, mid)
        if c < k:
            lef = mid + 1
        else:
            ri = mid - 1
    return lef


tr = build_tree(arr)
res = []
for i in range(m):
    le, r, k = map(int, input().split())
    le -= 1
    r -= 1
    res_i = find_kth(tr, le, r, k)
    res.append(res_i + 1)
print(" ".join(map(str, res)))
