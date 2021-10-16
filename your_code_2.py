import pandas as pd
df = pd.read_csv('GoogleApps.csv')


#print(df.head())

#print(df.tail)

#print(df.describe())

print(df[df['Type'] == 'Paid']['Price'].min())
print('__________________________________')
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())
print('__________________________________')
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)
print('__________________________________')
print(df[df['Content Rating'] == 'Teen']['Size'].min())
print('__________________________________')
print(df[df['Reviews']])


# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?


# Чему равно медианное (median) количество установок (Installs)
# приложений из категории (Category) "ART_AND_DESIGN"?


# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?


# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?


# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?


# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?
