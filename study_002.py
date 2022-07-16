from unicodedata import name

a = 3
b = 2 
# 1.if分支结构
if a > b :
    print(a)
else :
    print(b)
print("-------------")

# 2.if elif 分支结构
if a > b :
    print(a)
elif a < b :
    print(a)
elif a == b :
    print(a + '' + b) 
print("-------------")

# 3. in range 遍历结构
for i in range(6):
    print(i)
print("-------------")

# 4. in zip 遍历结构
name = ['张飞','赵云']
age = [20, 18]
for n,a in zip(name, age):
    print(n, '===', a)
print("-------------")

# 5.打印下标和值
for i,n in enumerate(name):
    print(i, "==", n)