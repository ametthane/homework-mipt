import numpy as np
import random

def gauss(n, a, b, noise_std = 1.0):
    x = np.random.uniform(0, 10, n)
    y = np.array([a * xi + b + random.gauss(0, noise_std) for xi in x])
    m = np.vstack([x, np.ones(n)]).T
    a_g, b_g = np.linalg.lstsq(m, y, rcond=None)[0]
    return x, y, a_g, b_g


N = int(input())
a, b = map(float, input().split())
x, y, a_g, b_g = gauss(N, a, b)
print("\nСгенерированные данные (x, y):")
for xi, yi in zip(x, y):
    print(f"({xi:.1f}, {yi:.1f})")
print("\nОценка коэффициентов МНК:")
print(f'a = {a_g:.2f}, b = {b_g:.2f}')

# Особая благодарность ИИ-модели Chat GPT за помощь с решением