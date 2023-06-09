# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

df = pd.read_csv('DZ09/sample_data/california_housing_train.csv')

popul = df['population'].min()

filt = df[df['population'] == popul]

households = filt['households'].max()

print("Максимальное значение households = ", households)