# Задача 40: Работать с файлом california_housing_train.csv, 
# который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


# ____________________
import pandas as pd
import os

dir = os.getcwd()
print(f'программа стартовала с папки {dir}')


df = pd.read_csv('DZ09/sample_data/california_housing_train.csv')
filt = df[(df['population'] >= 0) & (df['population'] <= 500)]
medianHouseValue = filt['medianHouseValue'].mean()
print(f'Средняя стоимость дома = {medianHouseValue:.2f} долларов.')
