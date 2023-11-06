import socket
import datetime

def create_event_log(connection_start_time, connection_end_time, transmitted_string, transmission_time):
    log = f"Connection start time: {connection_start_time}\n"
    log += f"Connection end time: {connection_end_time}\n"
    log += f"Transmitted string: {transmitted_string}\n"
    log += f"Transmission time: {transmission_time}\n"
    return log

def run_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        connection_start_time = datetime.datetime.now()
        transmitted_string = ""
        
        while True:
            user_input = input("Enter characters: ")
            if user_input == "disconnect":
                client_socket.send(user_input.encode())
                break
            
            transmitted_string += " " + user_input
            client_socket.send(user_input.encode())
            
            data = client_socket.recv(1024).decode()
            print("Received:", data)
            if data == "Connection closed":
                break
        
        connection_end_time = datetime.datetime.now()
        transmission_time = connection_end_time - connection_start_time
        
        event_log = create_event_log(connection_start_time, connection_end_time, transmitted_string, transmission_time)
        
        with open(".\event_log.txt", "w") as file:
            file.write(event_log)
        
        client_socket.close()
        print("Connection closed")

# Запуск клиента
run_client('192.168.0.175', 8000)

'''
Чтобы отслеживать нажатия клавиш в консоли, вы можете использовать библиотеку `keyboard` (не встроенная, необходимо установить). Однако, учет нажатий на клавиши в режиме реального времени может быть сложен, поскольку это включает многопоточность и не блокирующий ввод. 

Более того, библиотека `keyboard` может потребовать административных прав для работы, поскольку она использует глобальные события клавиатуры.

Вот пример того, как вы могли бы прослушивать нажатия клавиши "home":

```python
import keyboard

def run_client(host, port):
    global transmitted_string  # make it global to modify from the callback
    transmitted_string = ""

    def on_home(e):
        global transmitted_string
        # Send the data when 'home' key is pressed
        client_socket.send(transmitted_string.encode())
        transmitted_string = ""  # Clear the string

    keyboard.on_press_key('home', on_home)  # Setup the callback

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # ...your code...

        while True:
            user_input = input("Enter characters: ")
            if user_input == "disconnect":
                client_socket.send(user_input.encode())
                break

            transmitted_string += user_input

            # ...your code...
```

Помните, что этот код захватывает глобальное нажатие клавиши "home", что означает, что он будет срабатывать независимо от того, активно ли окно консоли.
'''