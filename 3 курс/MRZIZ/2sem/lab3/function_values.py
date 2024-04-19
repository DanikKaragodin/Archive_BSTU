import csv
import numpy as np

# Создать список пар значений x, y
x = np.linspace(0, 1000, 1000)
y = 0.1 * np.cos(0.1 * x) + 0.05 * np.sin(0.1 * x)

# Сохранить пары значений в CSV-файл
with open('function_values.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(y))
