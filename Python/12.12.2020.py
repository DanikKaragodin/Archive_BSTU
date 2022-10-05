import random


class FIFO:
    def __init__(self):
        self.FIFO = []

    def push(self, x):
        self.FIFO.insert(0,x)
        return self.FIFO[0]
    def delete(self):
        try:
            return self.FIFO.pop(-1)
        except IndexError:
            return "Очередь пуста"

    def watch(self, x):
        try:
            return self.FIFO[x]
        except IndexError:
            return "Такого элемента в очереди нет"

    def count(self):
        return len(self.FIFO)
    def is_empty(self):
        return (len(self.FIFO) == 0)


someFIFO = FIFO()
for i in range(random.randint(5, 50)):
    print(someFIFO.push(i),end=" ")

print(someFIFO)

for i in range(someFIFO.count()):
    print(someFIFO.delete(), end=" ")

print("")
print(someFIFO.delete())
