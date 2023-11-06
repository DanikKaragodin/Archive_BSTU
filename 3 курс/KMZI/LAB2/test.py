import struct
import hashlib

# Шаги из спецификации SHA-1
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
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

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

# Пример использования
message = "Hello"
sha1_hash = sha1(message)
print("SHA-1 хеш для сообщения:", sha1_hash)

# Сравнение с использованием библиотечной функции hashlib
hashlib_sha1 = hashlib.sha1()
hashlib_sha1.update(message.encode('utf-8'))
print("SHA-1 хеш с использованием hashlib:", hashlib_sha1.hexdigest())
