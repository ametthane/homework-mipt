import numpy as np

def lsm(x, y):
    x = np.array(x)
    y = np.array(y)
    m = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(m, y, rcond=None)[0]
    return a, b


x = list(map(int, input().split()))
y = list(map(int, input().split()))
a, b = lsm(x, y)
print(f"y = {a:.1f}*x + {b:.1f}")