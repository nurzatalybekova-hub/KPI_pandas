import pandas as pd

df = pd.read_excel('data_sales.xlsx')

# удалить пустые столбцы
# df = df.drop(columns=['Unnamed: 5', 'Unnamed: 6'])

# удалить пустые строки
# df = df.dropna(subset=['invoice_number'])

# проверить
# print(df.shape)
# print(df.columns)
# df.to_excel("sales_clean.xlsx", index=False)
# print(df['description'].nunique())
# # print(df['description'].unique())
# print(df['description'].value_counts().head(20))

# print(df['description'].nunique())
# print(df['buyer'].nunique())
# print(df['total'].sum())
# print(df['description'].value_counts().head(10))

# import pandas as pd

# profit_df = pd.read_excel(
#     r"C:\Users\Dell\Desktop\PYTHON DA8\numpy_pandas\profit_df.xlsx",
#     header=5
# )
# # print(profit_df.head())
# profit_df = profit_df.loc[:, ~profit_df.columns.str.contains('^Unnamed')]
# # print(profit_df.shape)
# # print(profit_df.columns)
# # print(profit_df.columns.to_list())
# print(profit_df.isna().all(axis=1).sum())
# profit_df.to_excel("profit_clean.xlsx", index=False)

import os
# print(os.getcwd())
pd.read_excel(r"C:\Users\Dell\Desktop\mini_project\sales_raw.xlsx")