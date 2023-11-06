import random
import numpy as np

class Network:
    def __init__(self) -> None:
        self.W = np.array([0.1, 0.8])
        self.func = lambda x: 3 if x >= -1 else -5
        self.a = 0.001

    def train(self, input_data: np.array, reference_data: np.array):
        epoch = 0
        while True:
            epoch += 1
            E = 0
            print(f"Эпоха №{epoch}: W - {self.W}]")
            for input, reference in zip(input_data, reference_data):
                output = self.func(input @ self.W)
                error = output - reference
                self.W -= self.a * input * (error)
                E += abs(error)
            if E == 0:
                break
            
        print(f"Всего эпох {epoch}")
    
    def sort(self, input):
        return self.func(input @ self.W)


input_data = np.array([[0, 0], [0, 6], [6, 0], [6, 6]])
reference = np.array([3, 3, -5, -5])

NN = Network()
NN.train(input_data, reference)
print("X1 - 0 X2 - 0 : ",NN.sort(np.array([0,0])))
print("X1 - 0 X2 - 6 : ",NN.sort(np.array([0,6])))
print("X1 - 6 X2 - 0 : ",NN.sort(np.array([6,0])))
print("X1 - 6 X2 - 6 : ",NN.sort(np.array([6,6])))

#a=random.randint(-10, 10)
#b=random.randint(-10, 10)
#for i in range(10):
#	a=random.randint(-10, 10)
#	b=random.randint(-10, 10)
#	print(f"x1: {a} x2: {b} y: {NN.sort(np.array([random.randint(-10, 10), random.randint(-10, 10)]))}")