# 模块的引用

# 1.引入方法
from common import sum

print(sum(12, 13))

# 2.引入对象
from common import Computer

com1 = Computer('华为', '平板电脑', 2000.00, '16G', '凌动')
com1.open()
com1.play()
com1.close()
com1.show_all()

# 3.引入方法
import common
print(common.sum(1, 4))

# 4.按模块引入
from module.tep_fun import show_date
show_date()

# 5.按模块引入对方法起别名
from module.tep_fun import show_date as sd
sd()

# 6.引入第三方模块
# pip install pymysql
'''
Collecting pymysql
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out. (read timeout=15)")': /packages/4f/52/a115fe175028b058df353c5a3d5290b71514a83f67078a6482cff24d6137/PyMySQL-1.0.2-py3-none-any.whl
  Downloading PyMySQL-1.0.2-py3-none-any.whl (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.8/43.8 KB 2.1 MB/s eta 0:00:00
Installing collected packages: pymysql
Successfully installed pymysql-1.0.2
WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
You should consider upgrading via the 'G:\software\python\python.exe -m pip install --upgrade pip' command.
'''

# 7.切换镜像
# 7.1.当前用户创建pip文件夹 C:\Users\Administrator\pip
# 7.2.创建pip.ini文件
'''
[global]
	index-url=https://pypi.tuna.tsinghua.edu.cn/simple
[install]
	trusted-host=pypi.tuna.tsinghua.edu.cn
'''