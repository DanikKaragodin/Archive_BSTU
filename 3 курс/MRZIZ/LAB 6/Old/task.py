from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from scipy.special import expit
import time
E_arr = []

class Perceptron:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.05):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.start_rate = learning_rate
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))
        # print(self.weights_input_hidden)
        # print(self.weights_hidden_output)

    def sigmoid(self, x):
        return expit(x)

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return self.output

    def backward(self, inputs, target, output):
        error = target - output
        delta_hidden = error.dot(self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_output)

        self.weights_hidden_output += self.hidden_output.T.dot(error) * self.learning_rate
        self.bias_output += np.sum(error, axis=0, keepdims=True) * self.learning_rate
        self.weights_input_hidden += inputs.T.dot(delta_hidden) * self.learning_rate
        self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * self.learning_rate
    def train(self, inputs, targets, epochs: int,isAdapt:bool = False):
        global E_arr
        for epoch in range(epochs):
            e_arr = []
            for i in range(len(inputs)):
                input_data = np.array([inputs[i]])
                target_data = np.array([targets[i]])
                output = self.forward(input_data)
                e_arr.append(target_data - output)
                self.backward(input_data, target_data, output)
            E2 = np.sum(np.array(e_arr)**2)/2
            E_arr.append(E2)
            self.learning_rate = self.start_rate*(1.0 / (1.0 + epoch/100)) if isAdapt else self.learning_rate
            #print(f"Online: Epoch: {epoch} MSE: {E2} LR: {self.learning_rate}")
    
    def backwardBatch(self, inputs, targets, outputs): 
        error = (targets.T - outputs).T
        mse_batch = np.sum(error)/len(error)
        inputs_cut = 0
        for j  in range(len(error)): inputs_cut += error[j]*inputs[j]
        mse_batch = np.array(mse_batch)
        inputs_cut = np.array(inputs_cut).reshape(1,-1)
        delta_hidden = mse_batch.dot(self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_output)
        self.weights_hidden_output += self.hidden_output.T.dot(mse_batch) * self.learning_rate
        self.bias_output += np.sum(mse_batch, axis=0, keepdims=True) * self.learning_rate
        self.weights_input_hidden += inputs_cut.T.dot(delta_hidden) * self.learning_rate
        self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * self.learning_rate
    def trainBatch(self,inputs,targets,epochs: int,batchsize: int, isAdapt: bool = False):
        global E_arr
        if(len(inputs) % batchsize != 0):
            print("Плохое значение пакета")
            return ValueError
        inputspack= [inputs[i-batchsize:i] for i in range(batchsize,len(inputs),batchsize)]
        targetspack= [targets[i-batchsize:i] for i in range(batchsize,len(targets),batchsize)]
        for epoch in range(epochs):
            e_arr = []
            for i in range(len(inputspack)):
                outputs = [self.forward(batchElem).item() for batchElem in inputspack[i]]
                for j in range(len(targetspack[i])): e_arr.append(targetspack[i][j]-outputs[j])
                self.backwardBatch(inputspack[i], targetspack[i], outputs)
            E2 = np.sum(np.array(e_arr)**2)/2
            E_arr.append(E2)
            self.learning_rate = self.start_rate*(1.0 / (1.0 + epoch/100)) if isAdapt else self.learning_rate
            #print(f"Batch: Epoch: {epoch} MSE: {E2} LR: {self.learning_rate}")

    def predict(self, inputs):
        output = self.forward(inputs)
        return output

if __name__ == "__main__":
    import csv

    epochs = 100
    X, Y = [], []
    with open(r"C:\Users\Danik\Documents\3 Kurs\MRZIZ\LAB 6\Old\diabetes.csv") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            X.append([float(value) for value in row[:-1]])
            Y.append([float(row[-1])])
    X = np.array(X)
    Y = np.array(Y)
    X /= 1000

    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    perceptron = Perceptron(8, 1, 1)
    start = time.time()
    perceptron.train(X_train, y_train, epochs,False)
    end = time.time()
    temp = perceptron.predict(X_test)
    y_pred = (temp>0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Time taken: {(end-start):.03f}s")
    print(f"Точность модели : {accuracy:.2f}")
    print(f"Точность модели (MSE) : {min(E_arr):.10f}")
    plt.plot(range(epochs),E_arr,'-')
    E_arr.clear()
    print(classification_report(y_test, y_pred, zero_division=1))

    perceptron = Perceptron(8, 1, 1)
    start = time.time()
    perceptron.train(X_train, y_train, epochs,True)
    end = time.time()
    temp = perceptron.predict(X_test)
    y_pred = (temp>0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Time taken: {(end-start):.03f}s")
    print(f"Точность модели: {accuracy:.2f}")
    print(f"Точность модели (MSE) : {min(E_arr):.10f}")
    plt.plot(range(epochs),E_arr,'--')
    E_arr.clear()
    print(classification_report(y_test, y_pred, zero_division=1))
    
    perceptron = Perceptron(8, 1, 1)
    start = time.time()
    perceptron.trainBatch(X_train, y_train, epochs,2,False)
    end = time.time()
    temp = perceptron.predict(X_test)
    y_pred = (temp>0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Time taken: {(end-start):.03f}s")
    print(f"Точность модели: {accuracy:.2f}")
    print(f"Точность модели (MSE) : {min(E_arr):.10f}")
    plt.plot(range(epochs),E_arr,'-.')
    E_arr.clear()
    print(classification_report(y_test, y_pred, zero_division=1))

    perceptron = Perceptron(8, 1, 1)
    start = time.time()
    perceptron.trainBatch(X_train, y_train, epochs,2,True)
    end = time.time()
    temp = perceptron.predict(X_test)
    y_pred = (temp>0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Time taken: {(end-start):.03f}s")
    print(f"Точность модели: {accuracy:.2f}")
    print(f"Точность модели (MSE) : {min(E_arr):.10f}")
    plt.plot(range(epochs),E_arr,':')
    plt.legend(['Online-Const','Online-Adapt','Batch-Const','Batch-Adapt'],loc="upper right")
    plt.show()
    print(classification_report(y_test, y_pred, zero_division=1))