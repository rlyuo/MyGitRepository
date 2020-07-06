# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import ToolsClass.OperateLog

#从第一行第一列的表格开始写入全部数据
def write_excel_xls_All(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿

#在第i行第j列的表格中写入数据
def write_excel_xls_Part(path, sheet_name, value,i,j):
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    sheet.write(i, j, value)  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿


#在原有的表格数据基础上从第一行第一列的表格开始写入全部数据
def write_excel_xls_append_All(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿


#在原有的表格数据基础上在第i行第j列的表格中写入数据
def write_excel_xls_append_Part(path, value,i,j):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    new_worksheet.write(i, j, value)  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿

#读全部数据
def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    all_row_data=list()
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            dict_data = worksheet.cell_value(i, j)
            all_row_data.append(dict_data)
    return all_row_data

#读某一个单元格数据
def read_excel_xls_part(path,i,j):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    excelData = worksheet.cell_value(i, j)
    return excelData

#分割列表,myList是需要分割的列表，n是把多少个元素分割为一组
def split_data(myList,n):
    segmentation = [myList[i:i + n] for i in range(0, len(myList), n)]
    return segmentation



