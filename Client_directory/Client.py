import pyautogui
import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        print("Подключение...")
        client.connect(("192.168.0.167", 1234))
        print("Подключено!")
        while True:
            client.send(input().encode("utf-8"))
    except:
        print("Не удалось подключиться.")
        time.sleep(2)