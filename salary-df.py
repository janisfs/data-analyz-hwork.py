
import pandas as pd

df = pd.read_csv('dz.csv')
# print(df.head())

# df = pd.read_csv('dz.csv')
# print(df.info())

# df = pd.read_csv('dz.csv')
# print(df.describe())

df.fillna(0, inplace=True)  # Заменить все NaN на 0
print(df)

group = df.groupby('City')['Salary']. mean()
print(group)