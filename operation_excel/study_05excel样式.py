import xlwt

wb = xlwt.Workbook()
sh1 = wb.add_sheet('info')

ft = xlwt.Font()
ft.name = '宋体' # 字体
ft.colour_index = 2 # 颜色
ft.height = 20*18 #字号 20的倍数
ft.bold = True # 是否加粗
ft.italic = True # 是否斜体
ft.underline = True # 是否下划线

alignment = xlwt.Alignment()
# 1=左对齐 2=居中 3=右对齐
alignment.horz = 1
# 1=上对齐 2=居中 3=下对齐
alignment.vert = 2
# 自动换行
alignment.wrap = 1

# 调整单元格宽度高度
sh1.col(5).width = 30*256
# 高度调整模式为开启
sh1.row(6).height_mismatch = True
sh1.row(6).height = 10*256

sy = xlwt.XFStyle()
sy.font = ft
sh1.write(0,0,'神奇',sy)
wb.save('003.xlsx')