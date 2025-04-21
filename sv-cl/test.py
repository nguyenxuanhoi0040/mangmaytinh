import socket
import time
import random
HOST = '127.0.0.1'
PORT = 5000
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.connect((HOST, PORT))
for i in range(10):
    temp = round(random.uniform(20, 40), 2)
    message = f"{temp}"
    sever_socket.send(message.encode())
    print(f'Sent: {message}')
    time.sleep(2)
sever_socket.close()