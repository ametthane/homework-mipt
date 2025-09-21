import numpy as np

rc = list(map(int, input().split()))
rows = rc[0]
cols = rc[1]

matrix = np.zeros((rows, cols), dtype=int)
top = 0
bottom = rows - 1
left = 0
right = cols - 1
num = 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top, i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i, right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom, i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i, left] = num
            num += 1
        left += 1

res = matrix * np.arange(rows)[:, np.newaxis]
print(res)

# Особая благодарность ИИ-модели Deepseek за помощь с реализацией