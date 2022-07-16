# pip install xlrd
# 读取excel文件
import xlrd
wb = xlrd.open_workbook('002.xlsx')

# 获取sheets数量
print(f'当前Excel的sheets 数量有{wb.nsheets}个')
# 获取sheets名称
print(f'sheets的名称有:{wb.sheet_names()}')
# 获取工作簿
sh1 = wb.sheet_by_index(0)
sh1 = wb.sheet_by_name('图书')

# 获取内容
# 获取行列的个数
print(f'sheet里面有{sh1.nrows}行，{sh1.ncols}列')

# 获取一行
print(sh1.row_values(0))
print(sh1.row_values(1))
print('---------------------------------------')
# 获取一列
print(sh1.col_values(0))
print(sh1.col_values(1))
print('---------------------------------------')
# 获取单元格
print('第一行第一列的数据是：', sh1.cell_value(1,1))
print('第一行第一列的数据是：', sh1.cell(1,1).value)
print('第一行第一列的数据是：', sh1.row(1)[1].value)
print('---------------------------------------')
# 获取所有数据
for sh in wb.sheets():
    for row in range(sh.nrows):
        print(sh.row_values(row))

