# pip install xlutils
import xlrd
from xlutils.copy import copy

# 打开excel
wb = xlrd.open_workbook('002.xlsx')
# 复制一份
cwb = copy(wb)
# 获取sheet1
sh1 = cwb.get_sheet(0)
# 写入数据
sh1.write(2,0,'三国演义')
sh1.write(2,1,'大宋国际')
sh1.write(2,2,'99')
sh1.write(2,3,'施耐庵')
sh1.write(2,4,'1000')
# 保存数据
cwb.save('002.xlsx')