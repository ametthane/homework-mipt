import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('iris_data.csv')
plt.figure(figsize=(15, 8))


f = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
fl1 = data[data['Species'] == 'Iris-setosa']
fl2 = data[data['Species'] == 'Iris-versicolor']
fl3 = data[data['Species'] == 'Iris-virginica']
for i in range(6):
    plt.subplot(2, 3, i+1)
    if i <= 2:
        plt.scatter(fl1[f[0]], fl1[f[i+1]])
        plt.scatter(fl2[f[0]], fl2[f[i+1]])
        plt.scatter(fl3[f[0]], fl3[f[i+1]])
        plt.xlabel(f[0])
        plt.ylabel(f[i+1])
    if 2 < i <= 4:
        plt.scatter(fl1[f[1]], fl1[f[i-1]])
        plt.scatter(fl2[f[1]], fl2[f[i-1]])
        plt.scatter(fl3[f[1]], fl3[f[i-1]])
        plt.xlabel(f[1])
        plt.ylabel(f[i-1])
    if i == 5:
        plt.scatter(fl1[f[2]], fl1[f[3]])
        plt.scatter(fl2[f[2]], fl2[f[3]])
        plt.scatter(fl3[f[2]], fl3[f[3]])
        plt.xlabel(f[2])
        plt.ylabel(f[3])
        k, b = np.polyfit(data['PetalLengthCm'], data['PetalWidthCm'], 1)
        plt.plot(data['PetalLengthCm'], k * np.array(data['PetalLengthCm']) + b,
                 color='darkred', label=f'y = {k:.3f}·x + {b:.3f}')
        plt.legend()
plt.show()