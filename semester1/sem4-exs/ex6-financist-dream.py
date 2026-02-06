import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('BTC_data.csv')
data['time'] = pd.to_datetime(data['time'])

days = (data['time'] - data['time'].min()).dt.days
coeffs = np.polyfit(days, data['close'], 3)
poly = np.poly1d(coeffs)

plt.figure(figsize = (15,8))
plt.plot(data['time'], data['close'], alpha = 0.7, label = 'Фактическая цена')
plt.plot(data['time'], poly(days), label = 'Аппроксимация')
plt.title('Цена биткоина 2017-2023')
plt.xlabel('Дата')
plt.ylabel('Цена, $')
plt.legend()
plt.show()
