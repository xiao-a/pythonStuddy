def sum(a, b):
    return a + b


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
        print(f'{self.name}->{self.type} -> {self.price} -> {self.memory} -> {self.cpu}')


