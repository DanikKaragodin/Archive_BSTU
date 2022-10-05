import math
import random

class Vector:
    x1 = 0
    y1 = 0
    z1 = 0

    def __init__(self,x2,y2,z2):
        self.x1 = x2
        self.y1 = y2
        self.z1 = z2

    def vectorLength(self):
        return math.sqrt(math.pow(self.x1, 2) + math.pow(self.y1, 2) + math.pow(self.z1, 2))
        

    def scalarMultiplication(self, obj):
        return self.x1*obj.x1+self.y1*obj.y1+self.z1*obj.z1

    def vectorData(self):
        return self.x1, self.y1, self.z1

    def multiplicationOf_a_VectorWithAnotherVector(self, obj):
        return Vector(self.y1*obj.z1-self.z1*obj.y1, self.z1*obj.x1-self.x1*obj.z1, self.x1*obj.y1-self.y1*obj.x1)

    def angle(self, obj):
        return math.degrees(math.acos((self.scalarMultiplication(x, y, z))/(math.fabs(self.vectorLength())*math.fabs(self.vectorLength(x2=x, y2=y, z2=z)))))

    def sumVector(self, x2, y2, z2):
        return self.x1+x2, self.y1+y2, self.z1+z2

    def differenceVector(self, x2, y2, z2):
        return self.x1-x2, self.y1-y2, self.z1-z2

def vectorGenerate(count=1):
    for i in range(count):
        x=random.uniform(-100,100)
        y=random.uniform(-100,100)
        z=random.uniform(-100,100)     
        return Vector(x,y,z)
someVector = vectorGenerate()
someVector2 = vectorGenerate()
print(someVector.vectorData())
print(someVector2.vectorData())
print(someVector.scalarMultiplication(someVector2))
