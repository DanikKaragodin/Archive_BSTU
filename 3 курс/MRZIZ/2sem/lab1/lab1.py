import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
# Загрузка данных из файла CSV
data = pd.read_csv("Seed_Data.csv")

# Извлечение вещественных атрибутов
attributes = data.iloc[:, :-1].values

# Среднее значение для центрирования данных
mean_values = np.mean(attributes, axis=0)

# Центрирование данных
centered_data = attributes - mean_values

start_time = time.time()
# Ковариационная матрица
covariance_matrix = np.cov(centered_data, rowvar=False)

# Вычисление собственных значений и собственных векторов

eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
end_time = time.time()

# Вывод времени выполнения
print(f"Время выполнения PCA: {end_time - start_time:.5f} секунд")

# Сортировка собственных значений и векторов в убывающем порядке
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Количество компонент для сохранения
num_components = 2

# Выбор заданного количества компонент
selected_components = eigenvectors[:, :num_components]

# Преобразование данных в новое пространство
transformed_data = np.dot(centered_data, selected_components)

# Восстановление данных из преобразованных данных
reconstructed_data = np.dot(transformed_data, selected_components.T) + mean_values

# Расчет среднеквадратичного отклонения (MSE)
mse = np.mean((attributes - reconstructed_data)**2)

# Вывод ошибки
print(f"\nСреднеквадратичное отклонение (MSE) между оригинальными и восстановленными данными: {mse:.5f}")

# Вывод результата
print("\nПреобразованные данные после PCA:")
print(pd.DataFrame(transformed_data, columns=[f"PC{i+1}" for i in range(num_components)]))

# График данных и собственных векторов
plt.scatter(transformed_data[:, 0], transformed_data[:, 1], alpha=0.7)
plt.title('Biplot: Transformed Data')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()