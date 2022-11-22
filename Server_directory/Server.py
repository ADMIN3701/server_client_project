import socket, pyautogui
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.167", 1234))
server.listen(1)

while True:
    try:
        print("Подключие...")
        user, adres = server.accept()
        print("Подключено!")
        while True:
            data = user.recv(16).decode("utf-8")
            bit_data = data.split(" ")

            print(data)

            if data:
                os.system(f"{data}")

                if bit_data[0] == "/e": ######## доработать удаленную вставку текста
                    pyautogui.typewrite(bit_data[1:])
                    pyautogui.press("enter")
    except:
        print("Не удалось подключиться к клиенту.")
