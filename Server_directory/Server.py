import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(1)
while True:
    try:
        user, adres = server.accept()
        while True:
            user.send(input("enter").encode("utf-8"))
    except:
        print("соединение разорвано")