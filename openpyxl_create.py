# -*- encoding: utf-8 -*-
'''
@File    :   openpyxl_create.py
@Time    :   2021/09/28 00:12:04
@Author  :   希瓦 
'''


from  openpyxl import  Workbook 

wb = Workbook()
ws = wb.active
ws['A1'] = 42
ws.append([1, 2, 3])
wb.save("sample.xlsx")