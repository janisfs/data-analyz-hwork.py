import pandas as pd

# вывести первые 5 строк
df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
print(df.head())

# вывести последние 5 строк
df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
print(df.tail())

# вывести информацию о датафрейме
df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
print(df.info())

# вывести описательные статистики
df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
print(df.describe())