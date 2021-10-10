# -*- encoding: utf-8 -*-
'''
@File    :   pandas_read_excel.py
@Time    :   2021/10/08 22:33:43
@Author  :   希瓦 
'''


import pandas as pd

# df = pd.read_excel('2.xlsx',engine='openpyxl')
# print(df)
# df.loc[1] = ['x2','学科辅导','校内','按课包收费',0,0,100]
# index = df.index
# # df.drop(index=1,inplace = True)
# print('yyyyyyyyyyyyyyyyy',index)
# print('---------------------------- /n',df)
# # df.to_excel('2.xlsx',index=False)



# def  add_a_row

df1 = pd.read_excel('t.xlsx',engine='openpyxl')
df2 = pd.DataFrame({'A':[1,2,3,4,5],'B':[5,6,7,8,9]})
df1 = df1.append(df2,ignore_index=True)
print(df1)
df1.to_excel('t.xlsx',index=False)