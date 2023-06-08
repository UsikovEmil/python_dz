# Задача 40: Работать с файлом california_housing_train.csv, 
# который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


# ____________________
# import pandas as pd

# # Загрузка файла и создание DataFrame

# # df = pd.read_csv('sample_data/california_housing_train.csv')
# df = open('E:\C#\Python\python_dz\DZ09\sample_data\california_housing_train.csv')

# # Фильтрация строк по значению population
# df_filtered = df[(df['population'] >= 0) & (df['population'] <= 500)]

# # Вычисление средней стоимости дома
# mean_house_value = df_filtered['median_house_value'].mean()

# print(f'Средняя стоимость дома с количеством людей от 0 до 500 равна {mean_house_value:.2f} долларов.')
# ----------------------
import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

filtered_df = df[(df['population'] >= 0) & (df['population'] <= 500)]

print(filtered_df.head(10))

mean_house_valie = filtered_df['median_house_value'].mean()

print('Средняя стоимость дома, где количество людей от 0 до 500 --> ', mean_house_valie)