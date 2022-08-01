# pip install xlwt
# 创建excel表格
import xlwt
wb = xlwt.Workbook()
sh1 = wb.add_sheet('图书')

sh1.write(0,0,'书名')
sh1.write(0,1,'出版商')
sh1.write(0,2,'价格')
sh1.write(0,3,'作者')
sh1.write(0,4,'库存')

sh1.write(1,0,'水浒传')
sh1.write(1,1,'大宋国际')
sh1.write(1,2,'99')
sh1.write(1,3,'施耐庵')
sh1.write(1,4,'1000')


sh1.write(2,0,'隋唐演义')
sh1.write(2,1,'大唐国际')
sh1.write(2,2,'88')
sh1.write(2,3,'不清楚')
sh1.write(2,4,'888')


sh1.write(3,0,'三国演义')
sh1.write(3,1,'后焊国际')
sh1.write(3,2,'66')
sh1.write(3,3,'不清楚')
sh1.write(3,4,'777')


wb.save("004.xlsx")