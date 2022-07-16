import os

# 1.拼接目录
# r 是转义字符
print(os.path.join(r'python\base', 'day01'))

# 2.打印当前位置
print(os.getcwd())

print(os.path.join(os.getcwd(), 'day02/file'))

# 3.绝对路径
print(os.path.abspath('common.py'))

# 4.查看是否存在
print(os.path.exists('common'))
print(os.path.exists('module'))

# 5.如果excel文件夹不存在就去创建
if not os.path.exists('excel'):
    os.makedirs('excel')