# ================================
# ЗАДАЧИ ПО PANDAS (СТУДЕНТЫ)
# Файл: students.xlsx
# Столбцы:
# id, first_name, last_name, age, gender, group, q1, q2, q3, q4

# q1,q2,q3,q4 - это столбцы которые хранят оценки за четверть

# ================================

# 1. Загрузить Excel файл в DataFrame и вывести первые 10 строк

import pandas as pd

df = pd.read_excel('students.xlsx')
# print(df.head(10))
# --------------------------------
# 2. Добавить новый столбец avg_score (средний балл q1-q4)
df['avg_score'] = df[['q1','q2','q3','q4']].mean(axis=1)
# print(df)
# --------------------------------
# 3. Вывести студентов, у которых avg_score >= 4.5 (отличники)
# print(df[df['avg_score']>=4.5])

# --------------------------------
# 4. Отфильтровать студентов по группе (например group == "A1")
grp = df.groupby('group')['id'].count()
# print(grp)
# print(df[df['group']=='A1'])

# --------------------------------
# 5. Найти максимальный балл по каждой четверти (q1, q2, q3, q4)
max_q1 = df['q1'].max()
max_q2 = df['q2'].max()
max_q3 = df['q3'].max()
max_q4 = df['q4'].max()
# print(max_q1, max_q2, max_q3, max_q4)

# --------------------------------
# 6. Найти самого младшего студента (min age) ????
min_age = df['age'].min()
# print(min_age)
# print(df['age']=df['age'].min())????
# --------------------------------
# 7. Посчитать средний avg_score по каждой группе (groupby group)
grp = df.groupby('group')['avg_score'].mean()
# print(grp)


# --------------------------------
# 8. Посчитать количество студентов по полу (gender)
grp = df.groupby('gender')['id'].count()
# print(grp)

res = pd.pivot_table(
    df, 
    values='id', 
    index='gender', 
    columns = 'group', 
    aggfunc = 'count' 
)
# print(res)
# --------------------------------
# 9. Найти сумму всех оценок по каждой четверти (q1-q4)
sum_q1 = df['q1'].sum()
sum_q2 = df['q2'].sum()
sum_q3 = df['q3'].sum()
sum_q4 = df['q4'].sum()
# print(sum_q1, sum_q2, sum_q3, sum_q4)
# print(df['q1'].sum())
# --------------------------------
# 10. Вывести топ-3 студентов в каждой группе по avg_score
# =================================
top3 = (
    df.sort_values(['group', 'avg_score'],
                   ascending=[True, False])
      .groupby('group')
      .head(3)
)
print(top3)

top3.to_excel('students_results.xlsx', index = False)
#Sultan
print(df.sort_values('avg_score', acsending=False).groupby('group').head(3))

print('hello')
