# -*- encoding: utf-8 -*-
'''
@File    :   openpyxl_open_exist.py
@Time    :   2021/09/28 00:13:28
@Author  :   希瓦 
'''


from openpyxl import load_workbook

class ExceclTool:

    @classmethod
    def  modify_cells(cls,file_path,cells_and_value:dict = None):
    
        wb = load_workbook(file_path)
        ws = wb.active
        for i in cells_and_value.keys():
            ws[i]=cells_and_value[i]
        wb.save(file_path)

if __name__ == '__main__':
    ExceclTool.modify_cells(file_path='1.xlsx',cells_and_value={'A3':'007','B3':'HEHE'})






