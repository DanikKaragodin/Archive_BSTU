import socket
def process_group(group):
    unique_chars = set(group)
    if len(unique_chars) < 3:  # Если число разных символов меньше 3, разрываем соединение
        return None
    result = []
    for char in unique_chars:
        count = group.count(char)
        result.append(f"{char}-{count}")
    return ', '.join(result)
def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Слушает сервер на {host}:{port}")
        while True:
            try:
                data, addr = server_socket.recvfrom(64)
                print(f"Замечен пользователь на {addr}")
                while data:
                    result = process_group(data.decode())
                    if result is None:  # Если число разных символов меньше 3
                        server_socket.sendto(b"Connection closed",addr)
                        break    
                    server_socket.sendto(result.encode(),addr)
                    data,addr = server_socket.recvfrom(64)
            except socket.error:
                print(f"ОШИБКА! {socket.error}")
                break
# Запуск сервера
run_server('192.168.0.175', 8000)
