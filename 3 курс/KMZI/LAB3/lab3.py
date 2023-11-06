import random
import math

def is_coprime(a, b):
    # Проверка на взаимную простоту двух чисел
    return math.gcd(a, b) == 1

def generate_key(p, g):
    # Генерация секретного ключа
    private_key = random.randint(1, p - 1)

    # Вычисление открытого ключа
    public_key = pow(g, private_key, p)
    
    return private_key, public_key

def sign_message(message, p, g, private_key):
    while True:
        # Генерация случайного числа k
        k = random.randint(1, p - 2)
        
        if is_coprime(k, p - 1):
            break
    
    # Вычисление первой компоненты подписи (r)
    r = pow(g, k, p)
    
    # Вычисление второй компоненты подписи (s)
    inverse_k = pow(k, -1, p - 1)
    hash_message = hash(message)  # Здесь может быть использован любой хеш-алгоритм
    s = (hash_message - private_key * r) * inverse_k % (p - 1)
    
    return r, s

def verify_signature(message, signature, p, g, public_key):
    r, s = signature
    
    # Вычисление левой и правой частей равенства для проверки подписи
    left_side = pow(g, hash(message), p)
    right_side = (pow(public_key, r, p) * pow(r, s, p)) % p
    
    # Проверка подписи
    if left_side == right_side:
        return True
    else:
        return False

# Пример использования алгоритма
p = 23  # Простое число
g = 5   # Генератор поля

# Генерация ключей
private_key, public_key = generate_key(p, g)

# Подписание сообщения
message = "Hello, world!"
signature = sign_message(message, p, g, private_key)

# Проверка подписи
is_valid = verify_signature(message, signature, p, g, public_key)
print("Подпись верна:", is_valid)