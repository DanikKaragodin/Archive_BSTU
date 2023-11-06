import struct
import hashlib
import matplotlib.pyplot as plt
import os
def calculate_hash(file_path):
    with open(file_path,encoding="UTF-8",mode='r') as file:
        data = file.read()
        hash_object = sha1(data)
        return hash_object
def save_hash(file_path, hash_value):
    with open(file_path,encoding="UTF-8",mode= 'w') as file:
        file.write(hash_value)
def read_message(file_path):
    with open(file_path,encoding="UTF-8",mode= 'r') as file:
        return file.read()
def save_message(file_path, message):
    with open(file_path,encoding="UTF-8",mode= 'w') as file:
        file.write(message)
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff
def sha1(message):
    # Инициализация переменных
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Преобразование сообщения в байтовую строку
    message = bytearray(message, 'utf-8')

    # Добавление дополнительного бита и заполнение нулями
    length = (8 * len(message)).to_bytes(8, byteorder='big')
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += length

    # Вычисление хеша по блокам
    for i in range(0, len(message), 64):
        block = message[i:i+64]

        # Инициализация словами
        words = struct.unpack('>16L', block)

        # Инициализация расширенного блока
        w = list(words) + [0] * 64

        # Обработка расширенного блока
        for j in range(16, 80):
            w[j] = left_rotate((w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16]), 1)

        # Инициализация переменных хэша
        a,b,c,d,e = h0,h1,h2,h3,h4
        # Основной цикл
        for j in range(80):
            if j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Обновление хэш-значений
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    # Форматирование хэш-значения и возврат результата
    hash_value = '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)
    return hash_value

def count_changed_bits(hash1, hash2):
    """
    Функция для подсчета числа измененных бит между двумя хэшами.
    """
    hash1=str(hash1)
    hash2=str(hash2)
    count = 0
    for byte1, byte2 in zip(hash1, hash2):
        diff = int(byte1) ^ int(byte2)
        count += bin(diff).count('1')
    return count
def compute_hash(message):
    """
    Функция для вычисления хэша сообщения.
    """
    hash_values = []
    hash_obj = hashlib.sha1()
    hash_obj.update(message.encode('utf-8'))
    hash_values.append(int.from_bytes(hash_obj.digest(), 'big'))

    # Изменяем один бит в сообщении и пересчитываем хэш после каждого раунда
    for pos in range(len(message) * 8):
        modified_message = message[:pos // 8] + \
                           chr(ord(message[pos // 8]) ^ (1 << (7 - pos % 8))) + \
                           message[pos // 8 + 1:]
        
        hash_obj = hashlib.sha1()
        hash_obj.update(modified_message.encode('utf-8'))
        hash_values.append(int.from_bytes(hash_obj.digest(), 'big'))

    return hash_values
def plot_bit_changes(hash_values):
    """
    Функция для построения графика числа измененных бит в хэше от раунда вычисления хэш-функции.
    """
    rounds = range(len(hash_values)-1)
    bit_changes = [count_changed_bits(hash_values[i], hash_values[i+1]) for i in range(len(hash_values)-1)]
    plt.plot(rounds, bit_changes)
    plt.xlabel('Раунд вычисления хэша')
    plt.ylabel('Число измененных бит')
    plt.title('Зависимость числа измененных бит от раунда вычисления хэша')
    plt.show()

file_path = 'message.txt'
hash_path = 'hash.txt'

choice = ''

while choice != '5':
    print('Выберите действие:')
    print('1. Просмотреть сообщение')
    print('2. Изменить сообщение')
    print('3. Вычислить и сохранить значение хэш-функции')
    print('4. Лавинный эффект')
    print('5. Выйти')
    choice = input('Введите номер действия: ')
    os.system("cls")
    if choice == '1':
        message = read_message(file_path)
        print('Сообщение:', message)
    elif choice == '2':
        message = input('Введите новое сообщение: ')
        save_message(file_path, message)
        print('Сообщение успешно изменено.')
    elif choice == '3':
        hash_value = calculate_hash(file_path)
        save_hash(hash_path, hash_value)
        print('Значение хэш-функции сохранено.')
    elif choice == '4':
        message = read_message(file_path)
        hash_values = compute_hash(message)
        plot_bit_changes(hash_values)
        print('Изучение лавинного эффекта завершено.')
    elif choice == '5':
        print('Выход.')
    else:
        print('Некорректный выбор. Попробуйте снова.')