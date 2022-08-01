import xlrd
from xlutils.copy import copy

def read_data():
    wb = xlrd.open_workbook("004.xlsx")
    sh = wb.sheet_by_index(0)

    s_price_list = []

    for r in range(1,sh.nrows):

        # 获取表格中数据
        # print(sh.cell_value(r,2))
        # print(sh.cell_value(r,4))
        s_price = float(sh.cell_value(r,2)) * float(sh.cell_value(r,4))
        
        # 打印价格
        # print(s_price)
        s_price_list.append(s_price)

    # 打印返回的list
    print(s_price_list)
    # print(sum(s_price_list))
    return s_price_list

def save_data(spl):
    wb = xlrd.open_workbook("004.xlsx")
    sh1 = wb.sheet_by_index(0)
    wb2 = copy(wb)
    sh2 = wb2.get_sheet(0)

    # 添加单标价格
    for r in range(1,sh1.nrows):
        sh2.write(r, 5, spl[r-1])
    # 汇总
    sh3 = wb2.add_sheet('汇总数据')
    sh3.write(0,0,'总金额')
    sh3.write(0,1,sum(spl))
    wb2.save('005.xlsx')

        
s = read_data()
save_data(s)