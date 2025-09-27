import numpy as np
import matplotlib.pyplot as plt

sizes = [30, 150, 1000, 10000]
plt.figure(figsize=(15, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    data = np.random.normal(0, 1, sizes[i])
    plt.hist(data, bins=30, density=True, alpha=0.7)

    x = np.linspace(-4, 4, 100)
    y = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)

    plt.plot(x, y)
    plt.title(f'{sizes[i]} точек')
plt.show()

#Особая благодарность ИИ-модели Deepseek за помощь с математикой