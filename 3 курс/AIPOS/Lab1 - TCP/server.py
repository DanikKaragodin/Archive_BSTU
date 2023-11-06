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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection established from {addr}")
            
            data = client_socket.recv(64).decode()
            
            while data:
                result = process_group(data)
                if result is None:  # Если число разных символов меньше 3
                    client_socket.send(b"Connection closed")
                    break
                
                client_socket.send(result.encode())
                data = client_socket.recv(64).decode()
            
            client_socket.close()
            print(f"Connection closed from {addr}")

# Запуск сервера
run_server('192.168.0.175', 8000)
