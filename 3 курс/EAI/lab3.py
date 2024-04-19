import difflib
import tkinter as tk

# Задание 1: Функция вычисления редакционного расстояния
def edit_distance(str1, str2):
    m = len(str1) + 1
    n = len(str2) + 1
    t = [[i + j for j in range(n)] for i in range(m)]
    for i in range(1, m):
        c = i - 1
        for j in range(1, n):
            d = j - 1
            t[i][j] = min(t[c][j] + 1, t[i][d] + 1, t[c][d] + (str1[c] != str2[d]))
    return t[m - 1][n - 1]

# Задание 2: Внешний интерфейс GUI
root = tk.Tk()
root.title("Редакционное расстояние")

# Задание 3: Сервисные функции
def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def get_words(text):
    words = text.split()
    return words

# Задание 4: Реализация сервисных функций
text = load_text("index.html")
words = get_words(text)

# Задание 5: Тестирование
def calculate_distances():
    input_word = input_entry.get()
    max_distance = int(max_distance_entry.get())
    results = []
    for word in words:
        distance = edit_distance(input_word, word)
        if distance <= max_distance:
            results.append((word, distance))
    results.sort(key=lambda x: x[1], reverse=True)
    output_text.delete("1.0", tk.END)
    for word, distance in results:
        output_text.insert(tk.END, f"{word} ({distance})\n")

# Задание 6: Средства помощи пользователю
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Помощь")
    help_text = tk.Text(help_window)
    help_text.insert(tk.END, "Помощь\n\nВведите входное слово:\nВведите максимальное расстояние:\nПолучите перечень слов с расстоянием редактирования меньше или равным максимальному.")
    help_text.config(state="disabled")
    help_text.pack()

# Интерфейс
input_label = tk.Label(root, text="Введите входное слово:")
input_entry = tk.Entry(root)

max_distance_label = tk.Label(root, text="Введите максимальное расстояние:")
max_distance_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Вычислить", command=calculate_distances)
help_button = tk.Button(root, text="Помощь", command=show_help)

output_label = tk.Label(root, text="Результаты:")
output_text = tk.Text(root, height=10)

input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)

max_distance_label.grid(row=1, column=0)
max_distance_entry.grid(row=1, column=1)

calculate_button.grid(row=2, column=0, columnspan=2)
help_button.grid(row=3, column=0, columnspan=2)

output_label.grid(row=4, column=0)
output_text.grid(row=4, column=1)

root.mainloop()