class SetofStacks:
    maxX=10
    maxXConst=10
    def __init__(self):
        self.SetofStacks = []

    def push(self, x):
        self.SetofStacks.append(x)
        if len(self.SetofStacks)==self.maxX:
            self.maxX+=1
            bifferlist=[]
            bifferlist+=self.SetofStacks[len(self.SetofStacks)-self.maxXConst:len(self.SetofStacks)]
            print(bifferlist, "буфер лист")
            for c in range(self.maxXConst):
                self.SetofStacks.pop()
            self.SetofStacks.insert(self.maxX-self.maxXConst,bifferlist)
            print(self.SetofStacks, "стэк лист")    


    def pop(self):
        try:
            return self.SetofStacks.pop()
        except IndexError:
            return "SetofStacks is empty."

    def peek(self):
        try:
            return self.SetofStacks[0]
        except IndexError:
            return "SetofStacks is empty."

    def count(self):
        return len(self.SetofStacks)

someSetofStacks = SetofStacks()
for i in range(1,41):
    someSetofStacks.push(i)
