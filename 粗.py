
import xlrd
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
from datetime import date,datetime

file = 'BP_TaoAIR_V1.0_hvac_cost'
def read_excel():
    wb = xlrd.open_workbook(filename=file)#打开文件
sheet1 = wb.sheet_by_index(0)#通过索引获取表格
sheet2 = wb.sheet_by_name('年级')#通过名字获取表格

print(sheet3.cell(1,0).value)#获取表格里的内容，三种方式

print(sheet3.cell_value(1,0))

print(sheet3.row(1)[0].value)



