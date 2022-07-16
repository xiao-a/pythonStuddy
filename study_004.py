# 类
# 电脑-台式机，笔记本，服务器

class Computer:
    def __init__(self, name, type, price, memory, cpu):
        self.name = name
        self.type = type
        self.price = price
        self.memory = memory
        self.cpu = cpu

    def open(self):
        print(f'{self.name}开机中...')

    def play(self):
        print('打开电视...')

    def close(self):
        print(f'{self.name}关机中...')

    def show_all(self):
        print(self.name + '->' + self.type + '->' + self.price + '->' + self.memory + '->' + self.cpu)

com1 = Computer('联想', '台式机', 3000, '32G', 'i7-10805')
com1.open()
com1.play()
com1.close()
