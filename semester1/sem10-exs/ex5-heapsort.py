def heapify_max(a, n, i):
    le = 2 * i + 1
    ri = 2 * i + 2
    m = i
    if le < n and a[le] > a[m]:
        m = le
    if ri < n and a[ri] > a[m]:
        m = ri
    if m != i:
        a[i], a[m] = a[m], a[i]
        heapify_max(a, n, m)


def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify_max(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify_max(a, i, 0)


arr = list(map(int, input().split()))
heap_sort(arr)
print(' '.join(map(str, arr)))
