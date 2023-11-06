import socket
import datetime
import keyboard

def create_event_log(connection_start_time, connection_end_time, transmitted_string, transmission_time):
    log = f"Connection start time: {connection_start_time}\n"
    log += f"Connection end time: {connection_end_time}\n"
    log += f"Transmitted string: {transmitted_string}\n"
    log += f"Transmission time: {transmission_time}\n"
    return log

def run_udp_client(host, port):
    def on_home(e):
        global transmitted_string
        client_socket.sendto(transmitted_string.encode(), server_address)
        transmitted_string = ""

    global transmitted_string
    transmitted_string = ""
    server_address = (host, port)
    keyboard.on_press_key('home', on_home)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        connection_start_time = datetime.datetime.now()
        print(f"Connected to {host}:{port}")
        
        while True:
            user_input = input("Enter characters: ")
            if user_input.startswith("disconnect"):
                client_socket.sendto(user_input.encode(), server_address)
                break
            
            transmitted_string += user_input
            if len(transmitted_string) >= 64:  # send the data in chunks of 64
                transmitted_string = transmitted_string[:64]

            data = client_socket.recv(1024).decode()
            print("Received:", data)
        
        connection_end_time = datetime.datetime.now()
        transmission_time = connection_end_time - connection_start_time
        
        event_log = create_event_log(connection_start_time, connection_end_time, transmitted_string, transmission_time)
        
        with open("event_log.txt", "w") as file:
            file.write(event_log)
        
        client_socket.close()
        print("Connection closed")

# Запустить клиент
run_udp_client('localhost', 8000)

'''
Обратите внимание, что здесь мы используем UDP, поэтому функции "подключения" и "отключения" другие. Помимо этого, в этой реализации предполагается, что заявленные функции разрыва соединения и автоподключения включены.

Следует помнить, что функция input блокирует, так что если вы набрали символы и нажали HOME, не нажимая Enter, символы, которые вы ввели, не будут переданы серверу до тех пор, пока вы не нажмете Enter.

Библиотека keyboard может потребовать административных разрешений для работы.
'''