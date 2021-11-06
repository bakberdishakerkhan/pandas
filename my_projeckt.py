#место для твоего кода

import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')

print(df.info())
#print("Гипотезы:")
#print("1)Присутствие определенный комбинации 'актер-режиссер'повышает рейтинг фильма на metacritic")
#print("2)2006-2010 годах рейтинг фильмов были выше"
print("___________________")
df["Revenue (Millions)"].fillna(-1, inplace = True)
print(len(df[pd.isnull(df["Revenue (Millions)"])]))

print("__________________")
df["Metascore"].fillna(-1, inplace = True)
print(len(df[pd.isnull(df["Metascore"])]))

print("__________________")
print(df[df['Year'] == '2006']['Rating'].max())

