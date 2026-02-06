def heapify_min(a, n, i):
    le = 2 * i + 1
    ri = 2 * i + 2
    m = i
    if le < n and a[le] < a[m]:
        m = le
    if ri < n and a[ri] < a[m]:
        m = ri
    if m != i:
        a[i], a[m] = a[m], a[i]
        heapify_min(a, n, m)


def max_to_min_heap(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(a, n, i)


arr = list(map(int, input().split()))
max_to_min_heap(arr)
print(' '.join(map(str, arr)))
