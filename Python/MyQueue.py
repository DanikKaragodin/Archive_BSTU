class MyQueue:
    stack1=[]
    stack2=[]
    def __init__(self):
        self.MyQueue=[self.stack1,self.stack2]
    def pushInStackOne(self,x):
        self.stack1.append(x)
        return self.stack1[-1]
    def pushInStackTwo(self,x):
        self.stack2.append(x)
        return self.stack2[-1]
    def popInStackOne(self):
        try:
            return self.stack1.pop()
        except IndexError:
            return "Stack One is empty."
    def popInStackTwo(self):
        try:
            return self.stack2.pop()
        except IndexError:
            return "Stack Two is empty."
    def popQueue(self):
        try:
            return self.stack1.pop(0)
        except IndexError:
            try:
                return self.stack2.pop(0)
            except IndexError:
                return "Queue is empty."
    def count(self):
        return len(self.MyQueue)
someQueue=MyQueue()
for i in range(20):
    if (i<10):
        print(someQueue.pushInStackOne(i),end=",")
    else:
        print(someQueue.pushInStackTwo(i),end=";")
print()
for i in range(20):
    print(someQueue.popQueue(),end=".")
