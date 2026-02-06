import numpy as np
import matplotlib.pyplot as plt

u = [0.85289, 0.77067, 0.73460, 0.72403, 0.68594, 0.65082, 0.63111, 0.60419]
v = [0.38316, 0.29376, 0.26317, 0.25301, 0.21623, 0.18233, 0.16241, 0.13469]

k, b = np.polyfit(u, v, 1)

plt.title('Зависимость $T^2x_ц$ от $y^2$ для физического маятника')
plt.scatter(u, v, label='Исходные точки')
plt.plot(u, k*np.array(u) + b, color='red', label=f'v = {k:.3f}·u + {b:.3f}')
plt.xlabel('$y^2$')
plt.ylabel('$T^2x_ц$')
plt.legend()
plt.show()