import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iris_data.csv')
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)

sts_count = len(data[data['Species'] == 'Iris-setosa'])
versclr_count = len(data[data['Species'] == 'Iris-versicolor'])
vrgn_count = len(data[data['Species'] == 'Iris-virginica'])

sz = [sts_count, versclr_count, vrgn_count]
lab = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
col = ['lightblue', 'lavender', 'pink']

plt.pie(sz, labels=lab, colors=col, autopct='%1.1f%%')
plt.title('Разные виды ирисов')

plt.subplot(1, 2, 2)

s = len(data[data['PetalLengthCm'] <= 1.2])
m = len(data[(data['PetalLengthCm'] > 1.2) & (data['PetalLengthCm'] <= 1.5)])
l = len(data[data['PetalLengthCm'] > 1.5])

sz2 = [s, m, l]
lab2 = ['До 1.2 см', '1.2-1.5 см', 'Больше 1.5 см']
col2 = ['gold', 'darkorange', 'firebrick']

plt.pie(sz2, labels=lab2, colors=col2, autopct='%1.1f%%')
plt.title('Длина лепестка')

plt.show()

#Особая благодарность ИИ-модели Deepseek за помощь с оформлением