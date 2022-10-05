import random
class massive:
    firstmassive=[]
    secondmassive=[]
    thirdmassive=[]
    def __init__(self,a,b):
        self.firstmassive.extend(a)
        self.secondmassive.extend(b)
        for i in range(len(self.firstmassive)):
            self.thirdmassive.append(self.secondmassive[i]/sum(self.secondmassive))
        
    def returning(self):
        return self.firstmassive,self.secondmassive,self.thirdmassive
    def generate(self):
        randomvalue=random.uniform(0,1)
        count=0.0
        a=0
        for i in range(len(self.firstmassive)):
            if self.thirdmassive[i]+count>=randomvalue and randomvalue>=count:
                a=self.firstmassive[i]
                break
            else:
                count+=self.thirdmassive[i]
        return a
firstmassive=[1,2,3]
print(firstmassive)
ves=[1,2,10]
print(ves)
generatormassive=massive(firstmassive,ves)
print(generatormassive.returning())
print(generatormassive.generate())


         
