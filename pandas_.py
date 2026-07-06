import pandas as pd

df = pd.read_excel('titanic.xlsx')
# print(df)


array_1D = pd.Series([123,45,67,1,2,34])
# print(array_1D)

array_2D = pd.DataFrame({
    "name":["Tima", "Saule","Sultan"],
    "age":[20,30,25]
})
# print(array_2D)

c = ["name","age"]
array_2D = pd.DataFrame([
    ["Sultan",26],
    ["Saule",30]
], columns=c)

# print(c)

array_2D = pd.DataFrame([
    {"name":'Tima', "age":20},
    {"name":"Saule", "age":25}
])

# print(array_2D)

# print(df.head(10)) #печатает с начала
# print(df.tail(10)) # печатает с конца

# print(df.shape)
# print(df.columns) # посмотреть значения столбцов
# print(df.info()) # дает полное инфо

#-------Методы -------
# print(dir(df))

# print(df[(df['age']>20) & (df['survived']==1)])

# print(df[df['age']==df['age'].max()])
## df['age'].max() находим макс возраст
## df['age']==df['age'].max()] - отмечаем булевым знчанем True у которого возраст равен 62
# а тех пассажиров возраст не равен 62 False
## df[df['age']==df['age'].max()] - взяли пассажира, у которого отмечено True

series = pd.Series([12,23,5,23,0])
bool_array = series==5 #[False, True, False, True, False]
print(series[bool_array])

# print(df[["gender",'age',"id"]])
# print(df["gender"])

df.to_excel('result.xlsx')

# 4.1
# Найти пассажиров:
# - женского пола И возраст < 18
# print(df.dropna()) #не сохраняет изменения (пустые занчения). чтобы сохранить нужно дать название файлу и фохранить
# df = df.dropna()
# bool_array = (df["gender"]==1) & (df["gender"]<18)
# count_fm_18 = len(df[bool_array])

# 4.2
# Найти пассажиров:
# - 1 класса ИЛИ возраст меньше 10
# bool_array = df['pclass'] ==1 | (df["age"]<10)
# count_fc_10 = len(df[bool_array])

# 4.3
# Найти пассажиров, которые:
# - не выжили И были в 3 классе
# bool_array = (df['survived'] ==0) & (df['pclass']==3)
# count_dead_3c = len(df[bool_array])

# res = pd.DataFrame({
#     "Кол-во пассажиров женского пола младше 18 лет": [count_fm_18],
#     "Кол-во пассажиров 1 класса или младше 10 лет": [count_fc_10],
#     "Кол-во пассажиров 3 класса, которые не выжили": [count_dead_3c]
# })

# res.to_excel('resuls.xlsx', index=False)

'---------------------------------------------------------'

# 3.1
# # Сколько всего пассажиров в каждом классе (pclass)?
c1 = len(df[df['pclass']==1])
c2 = len(df[df['pclass']==2])
c3 = len(df[df['pclass']==3])
# print(count_1cl, count_2cl, count_3cl)
# 3.2
# Сколько мужчин и женщин в данных?
count_female = len(df[df['gender'] == 1])
count_male = len(df[df['gender'] == 0])

# print(count_female, count_male)
# 3.3
# Сколько выжило пассажиров в каждом классе?
c1s = len(df[(df['pclass'] == 1) & (df['survived'] ==1)])
c2s = len(df[(df['pclass'] == 2) & (df['survived'] ==1)])
c3s = len(df[(df['pclass'] == 3) & (df['survived'] ==1)])
# print(c1s, c2s, c3s)
# 3.4
# Средний возраст:
# - всех пассажиров
# - выживших
# - не выживших
total_avg = df['age'].mean()
survived_avg = df[df['survived']==1]['age'].mean()
dead_avg = df[df['survived']==0]['age'].mean()
# print(survived_avg)
data = {
    'cl':[c1], "c1":[c2], "c3":[c3],
    "male":[count_male], "female":[count_female],
    "c1s":[c1s], "c2s":[c2s], "c3s":[c3s],
    "total_avg":[total_avg], "survived_avg":[survived_avg], "dead_avg":[dead_avg]
}

df = pd.DataFrame(data)
df.to_excel('Result2.xlsx', sheet_name='index=False') #?????

df = pd.read_excel('titanic.xlsx')
# print(df['age'].describe()) # повзовляет использовать несколько данных

# print(df.isna()) # находит пустые значения, отмечает True -> dataframe с булевыми значениями
# print(df.dropna()) # удаляет пустные значения
# print(df.fillna(1)) # заполняет пустые значения

# df['is_adult'] = df['age']>=18
# print(df)
# df['status'] = ['Adult' if age>=18 else 'Child' for age in df['age']] #[A,A,A,A,Ch]
# print(df)

# grp = df.groupby('gender')['id'].count()
grp = df.groupby('gender')['age'].max()
# print(grp)
classes = df.groupby('pclass')
# print(classes)

# print(df.groupby('gender')['survived'].sum())

# list = [
#     [1,28,1],
#     [2,43,1],
#     [3,18,0],
#     [4,28,1],
#     [5,43,1],
#     [6,18,0]
# ]

res = pd.pivot_table(
    df, # датафрейм (таблица) по которой идет аналитика
    values='age', # это стоблбец по которому будет работать функция
    index='gender', # группировка с правой части (индекс)
    columns = 'pclass', # группировка сверху (столбцы)
    aggfunc = 'max' # функция, ктороая будет применять к столбцу в values
)
# print(res)


# res.to_excel('result5.xlsx', index = False)

# если бы не использовали pivot_table
# male = df[df['gender']==0]
# c1m = male[male['pclass']==1]['age'].max()
# c2m = male[male['pclass']==2]['age'].max()
# c3m = male[male['pclass']==3]['age'].max()

# female = df[df['gender']==1]
# c1f = male[male['pclass']==1]['age'].max()
# c2f = male[male['pclass']==2]['age'].max()
# c3f = male[male['pclass']==3]['age'].max()


df = pd.read_excel('products.xlsx')
'------------------------------------------------------'
# columns -> Название, цена, описание, сколько на складе категория товаров
# номер этих columns -> 0, 1, 2, 3, 4

# index -> 0, 1, 2, 3, 4 м.б.-> A, B, C, D, E..
# номер этих индексов -> 0, 1, 2, 3, 4, 5, 6...
# index - строки
# columns - стоблцы

# loc[название строки, название столбца]- обращение по названию строки иили столбца
# iloc[номер строки, номер столбца] - обращение по номеру строки или столбца
'----------------------------------------------------------'
# print(df)
# print(df.iloc[0,2]) # 1е число - это строка, 2е число - столбец
# print(df.iloc[:,2]) # выведет все индексы по столбцу 2
# print(df.iloc[0:5,2]) # выведет все индексы от 2 по 5 невключительно по столбцу 2

# print(df)
# print(df.iloc[0, 1])
# print(df.loc['Маска для лица C-396', 'Описание'])

# Достать цену "Планшет С-291" при помощи iloc, loc
print(df.iloc[92,1])
df = df.set_index('Название') # поменял индексацию(тоесть название строк) на названия продуктов
print(df.loc['Планшет C-291','Цена'])


