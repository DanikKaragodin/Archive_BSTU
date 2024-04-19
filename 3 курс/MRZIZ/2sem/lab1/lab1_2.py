import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
import matplotlib.pyplot as plt  # Add this line for matplotlib

# Загрузка данных из файла CSV
data = pd.read_csv("Seed_Data.csv")

# Извлечение вещественных атрибутов
attributes = data.iloc[:, :-1].values

# Нормализация данных
scaler = StandardScaler()
attributes_scaled = scaler.fit_transform(attributes)

# Преобразование в Tensor
tensor_data = torch.Tensor(attributes_scaled)

# Класс автоэнкодера
class Autoencoder(nn.Module):
    def __init__(self, input_size, encoding_size):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Linear(input_size, encoding_size)
        self.decoder = nn.Linear(encoding_size, input_size)

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Параметры автоэнкодера
input_size = attributes.shape[1]
encoding_size = 2

# Создание модели и оптимизатора
autoencoder = Autoencoder(input_size, encoding_size)
optimizer = optim.Adam(autoencoder.parameters(), lr=0.001)
criterion = nn.MSELoss()

# Создание DataLoader
batch_size = 32
dataset = TensorDataset(tensor_data, tensor_data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Обучение автоэнкодера
start_time = time.time()
num_epochs = 100
for epoch in range(num_epochs):
    for batch in dataloader:
        data_batch, _ = batch
        optimizer.zero_grad()
        outputs = autoencoder(data_batch)
        loss = criterion(outputs, data_batch)
        loss.backward()
        optimizer.step()

end_time = time.time()

# Вывод времени обучения
print(f"Время обучения автоэнкодера: {end_time - start_time:.5f} секунд")


autoencoder.eval()


with torch.no_grad():
    encoded_data = autoencoder.encoder(tensor_data)


encoded_data_np = encoded_data.numpy()

plt.scatter(encoded_data_np[:, 0], encoded_data_np[:, 1], c='b', marker='o', label='Encoded Data')
plt.title('Autoencoder Latent Space')
plt.xlabel('Latent Dimension 1')
plt.ylabel('Latent Dimension 2')
plt.legend()
plt.show()
# Вычисление ошибки между входными и восстановленными данными
with torch.no_grad():
    reconstructed_data = autoencoder(tensor_data)
    reconstruction_error = criterion(reconstructed_data, tensor_data)

# Вывод ошибки
print(f"Ошибка восстановления данных: {reconstruction_error.item():.5f}")

