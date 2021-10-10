# -*- encoding: utf-8 -*-
'''
@File    :   change_value.py
@Time    :   2021/10/10 23:20:14
@Author  :   希瓦 
'''

import pandas
import numpy
def modify_or_add_excel_rows(file_path, rows_and_values, sheet_name = 0, excel_type: str = 'xlsx'):
    '''
    修改或添加单行或多行数据
    :param file_path:
    :param rows_and_value: index:行标签值，excel默认是从0开始
    eg:{'2':[1,2,3],'3':[4,5,6]} 代表在第三行插入 1,2,3 第四行插入 4,5,6
    :param sheet_name: sheet名称
    :param excel_type: xlsx、xls
    :return:
    '''
    if excel_type == 'xlsx':
        print(file_path)
        df = pandas.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        print(type(df))
        print(111111111111111111111111111111)
    elif excel_type == 'xls':
        print(22222222222222222222222222222222)
        df = pandas.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')
    for i in list(rows_and_values.keys()):
        print(i)
        df.loc[i] = rows_and_values[i]
    df.to_excel(file_path,index=False)

def modify_or_add_excel_columns(file_path, columns_and_values, sheet_name = 0, excel_type: str = 'xlsx'):
    '''
    修改或添加单行或多行数据
    :param file_path:
    :param rows_and_value: index:行标签值，excel默认是从0开始
    eg:{'2':[1,2,3],'3':[4,5,6]} 代表在第三行插入 1,2,3 第四行插入 4,5,6
    :param sheet_name: sheet名称
    :param excel_type: xlsx、xls
    :return:
    '''
    if excel_type == 'xlsx':
        print(file_path)
        df = pandas.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        print(type(df))
        print(111111111111111111111111111111)
    elif excel_type == 'xls':
        print(22222222222222222222222222222222)
        df = pandas.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')
    for i in list(columns_and_values.keys()):
        print(i)
        df.loc[:,i] = columns_and_values[i]
    print(df)
    df.to_excel(file_path,index=False)

# modify_or_add_excel_columns('1.xlsx',{'m1':['m11',None],'m2':['m22',None]})


def modify_cell(file_path,row,column,value,sheet_name = 0,excel_type: str = 'xlsx'):
    if excel_type == 'xlsx':
        print(file_path)
        df = pandas.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        df.loc[row,column] = value
    elif excel_type == 'xls':
        df = pandas.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')
        df.loc[row,column] = value
    print(df)
    df.to_excel(file_path,index=False)

# modify_cell('1.xlsx',row = 1,column = 'Unnamed: 6',value = 100)

df = pandas.read_excel('tt.xlsx',engine='openpyxl')
print(df)