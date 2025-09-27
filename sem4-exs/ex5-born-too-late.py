import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('BTC_data.csv')
data['time'] = pd.to_datetime(data['time'])

plt.figure(figsize = (15,8))
plt.plot(data['time'], data['close'])
plt.title('Цена биткоина 2017-2023')
plt.xlabel('Дата')
plt.ylabel('Цена, $')
plt.show()
