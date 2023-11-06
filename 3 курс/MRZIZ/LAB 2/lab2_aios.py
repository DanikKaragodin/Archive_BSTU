import time
import numpy as np
from math import sin
from matplotlib import pyplot as plt

f = lambda x: 1 * sin(9 * x) + 0.5

class Network:
    def __init__(self, weights=np.random.rand(4, 1)/5, T=0.1, a=0.0046) -> None:
        self.weights = weights
        self.T = T
        self.a = a
    
    def predict(self, input: list) -> float:
        return np.sum(input @ self.weights) - self.T
    def reset(self):
        self.weights = np.random.rand(4, 1)/5
        self.T = 0.1
        self.a = 0.0046

    def trainConst(self, inputs, targets,epoch = 1000) -> list:
        global E_arr
        for i in range(epoch):
            for index, input in enumerate(inputs):
                prediction = self.predict(input)
                for j, w in enumerate(self.weights):
                    w[0] = w[0] - self.a * (prediction - targets[index]) * input[j]
                self.T = self.T + self.a * (prediction - targets[index])
                #print(f"step:{index+1}, weights={self.weights}")
            E,e_arr=0,[]
            for input, target in zip(inputs, targets):
                e_arr.append((NN.predict(input) - target) ** 2)
            E = 0.5 * np.sum(e_arr)
            if i == epoch-1: print("Эпоха:",i,"Квадратичная ошибка:", E)
            E_arr.append(E)

    def trainAdaptive(self, inputs, targets,epoch = 1000) -> list:
        global E_arr
        aplha = 0
        for i in range(epoch):
            for index, input in enumerate(inputs):
                prediction = self.predict(input)
                for j, w in enumerate(self.weights):
                    w[0] = w[0] - aplha * (prediction - targets[index]) * input[j]
                self.T = self.T + aplha * (prediction - targets[index])
                #print(f"step:{index+1}, weights={self.weights}")
            E,e_arr=0,[]
            for input, target in zip(inputs, targets):
                e_arr.append((NN.predict(input) - target) ** 2)
            E = 0.5 * np.sum(e_arr)
            aplha = self.a*E
            # Адаптивное изменение шага обучения
            if i == epoch-1: print("Эпоха:",i,"Квадратичная ошибка:", E,"Альфа",aplha)
            E_arr.append(E)
    # АЛЬФА НЕ ВЫШЕ a=0.0046
    def trainBatchConst(self,inputs,targets,epoch=1000,batchpack=4) -> list:
        global E_arr
        # Пакетное обучение
        for i in range(epoch):
            #print(len(inputs))
            inputspack= [inputs[i-batchpack:i] for i in range(batchpack,len(inputs),batchpack)]
            targetspack= [targets[i-batchpack:i] for i in range(batchpack,len(targets),batchpack)]
            err_arr = []
            for input,target in zip(inputspack,targetspack):
                # Рассчитываем предсказания модели
                predictions = np.array([self.predict(i) for i in input])
                # Рассчитываем ошибку
                error = predictions - target
                delta= np.zeros_like(self.weights.transpose())
                for j in range(error.size):
                    #print(delta,error[j],inputs[j])
                    delta = delta + (error[j]*input[j])
                E2 = 0
                for err in error:
                    E2+=err**2
                E2/=2
                err_arr.append(E2)
                self.weights = self.weights - self.a*delta.transpose()
                self.T = self.T + self.a * np.sum(error)
            E_arr.append(np.mean(err_arr))
    # АЛЬФА НЕ ВЫШЕ a=0.0046
    def trainBatchAdapt(self,inputs,targets,epoch=1000) -> list:
        global E_arr
        # Пакетное обучение
        for i in range(epoch):
            # Рассчитываем предсказания модели
            predictions = np.array([self.predict(i) for i in inputs])
            # Рассчитываем ошибку
            error = predictions - targets
            delta= np.zeros_like(self.weights.transpose())
            for j in range(error.size):
                #print(delta,error[j],inputs[j])
                delta = delta + (error[j]*inputs[j])
            E2 = 0
            for err in error:
                E2+=err**2
            E2/=2
            alpha = min(self.a*E2,0.0046)
            E_arr.append(E2)
            if i == epoch-1: print(i,E2,alpha)
            self.weights = self.weights - alpha * delta.transpose()
            self.T = self.T + alpha * np.sum(error)

# ДЛЯ 100 ТОЧЕК
x_100 = [el for el in np.arange(0, 1, 0.01)] # Разбиение на 100 точек
data = [f(el) for el in x_100] # Заполнение массива реальных значений функции
inputs = np.array([data[i-4:i] for i in range(4, len(data))]) # Создание массива входных значений
targets = data[4:] # Создание массива целевых значений
# ДЛЯ НЕИЗВЕСТНЫХ ТОЧЕК
x_60 = [el for el in np.arange(0.9, 1.5, 0.01)] # Разбиение на 60 точек
data2 = [f(el) for el in x_60] # Заполнение массива реальных значений функции
inputs2 = np.array([data2[i-4:i] for i in range(4, len(data2))])
targets2 = data2[4:] # Создание массива целевых значений

epoch=200
NN = Network()
func = {1: NN.trainConst, 2: NN.trainAdaptive, 3: NN.trainBatchConst, 4: NN.trainBatchAdapt}
for i in range(1):
    E_arr = []
    start = time.time()
    func[3](inputs, targets,epoch)
    end = time.time()
    print(f"Time taken: {(end-start)*10**3:.03f}ms")
    result = []
    for input in inputs2:
        result.append(NN.predict(input))
    plt.plot(range(epoch), E_arr)
    plt.show()
    plt.plot(x_100, data, x_60[4:], result, '--')
    plt.show()
    NN.reset()