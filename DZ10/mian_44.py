# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

OneHot = pd.DataFrame(0, index=data.index, columns=data['whoAmI'].unique(), dtype=int)

OneHot = OneHot.assign(**{col: (data['whoAmI'] == col).astype(int) for col in OneHot.columns})

print(OneHot)