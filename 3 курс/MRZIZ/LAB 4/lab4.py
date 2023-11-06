import numpy as np
from matplotlib import pyplot as plt
import time
#Ошибка (Массив)
Errors = []

# Инициализация весов сети
def initialize_weights(input_dim, hidden_dim, output_dim):
    #np.random.seed(0)
    W1 = np.random.randn(input_dim, hidden_dim)    # Веса первого слоя
    b1 = np.zeros((1, hidden_dim))                  # Смещение первого слоя
    W2 = np.random.randn(hidden_dim, output_dim)    # Веса второго слоя
    b2 = np.zeros((1, output_dim))                  # Смещение второго слоя
    return W1, b1, W2, b2

# Сигмоидная функция активации
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Производная сигмоидной функции
def sigmoid_derivative(x):
    return x * (1 - x)

# Функция обучения нейронной сети с одним скрытым слоем
def train(X, y, hidden_dim, epochs, learning_rate):
    global Errors
    input_dim = X.shape[1]
    output_dim = y.shape[1]

    # Инициализация весов
    W1, b1, W2, b2 = initialize_weights(input_dim, hidden_dim, output_dim)

    for epoch in range(epochs):
        # Прямое распространение
        hidden_layer = sigmoid(np.dot(X, W1) + b1)    # Выход скрытого слоя
        output_layer = sigmoid(np.dot(hidden_layer, W2) + b2)    # Выход сети

        # Ошибка
        error = y - output_layer
        mse = 0
        for i in error:
            mse+= i**2
        mse/=2
        Errors.append(mse)
        #print(mse)
        # Обратное распространение
        delta_output = error * sigmoid_derivative(output_layer)
        delta_hidden = np.dot(delta_output, W2.T) * sigmoid_derivative(hidden_layer)

        # Обновление весов
        W2 += learning_rate * np.dot(hidden_layer.T, delta_output)
        b2 += learning_rate * np.sum(delta_output, axis=0, keepdims=True)
        W1 += learning_rate * np.dot(X.T, delta_hidden)
        b1 += learning_rate * np.sum(delta_hidden, axis=0, keepdims=True)

    return W1, b1, W2, b2

# Тестирование обученной нейронной сети
def test(X, W1, b1, W2, b2):
    hidden_layer = sigmoid(np.dot(X, W1) + b1)
    output_layer = sigmoid(np.dot(hidden_layer, W2) + b2)
    return output_layer
    #return np.round(output_layer)

# Создание искусственного датасета XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Параметры обучения
hidden_dim = 4
epochs = 2500
learning_rate = 0.1

# Обучение нейронной сети
W1, b1, W2, b2 = train(X, y, hidden_dim, epochs, learning_rate)

# График ошибки
from matplotlib import pyplot as plt
plt.plot(range(epochs),Errors)
plt.show()
# Тестирование нейронной сети на новых примерах
X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = test(X_test, W1, b1, W2, b2)

# Вывод результатов
print("Predictions:")
for i in range(len(X_test)):
    print(f"{X_test[i]} -> {predictions[i]}")
