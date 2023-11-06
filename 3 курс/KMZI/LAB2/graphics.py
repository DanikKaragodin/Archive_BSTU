import hashlib
import matplotlib.pyplot as plt

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

# Пример использования
message = "Hello, world!"
hash_values = compute_hash(message)
plot_bit_changes(hash_values)
