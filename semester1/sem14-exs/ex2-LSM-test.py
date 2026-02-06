import numpy as np
import unittest


def lsm(x, y):
    x = np.array(x)
    y = np.array(y)
    m = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(m, y, rcond=None)[0]
    return a, b


class TestLSM(unittest.TestCase):
    def test_scaling_relationship(self):
        k = 2.5
        x = [0, 1, 2, 3, 4]
        y = [0, k, 2 * k, 3 * k, 4 * k]
        a, b = lsm(x, y)
        self.assertAlmostEqual(a, k)
        self.assertAlmostEqual(b, 0.0)

    def test_commutativity(self):
        x1 = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        c = 10
        x2 = [val + c for val in x1]
        a1, b1 = lsm(x1, y)
        a2, b2 = lsm(x2, y)
        self.assertAlmostEqual(a1, a2)

    def test_symmetry(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        ids = [2, 0, 4, 1, 3]
        xsh = [x[i] for i in ids]
        ysh = [y[i] for i in ids]
        a1, b1 = lsm(x, y)
        a2, b2 = lsm(xsh, ysh)
        self.assertAlmostEqual(a1, a2)
        self.assertAlmostEqual(b1, b2)


x = list(map(int, input().split()))
y = list(map(int, input().split()))
a, b = lsm(x, y)
print(f"y = {a:.1f}*x + {b:.1f}")
