import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 12345))

while True:
    data = input()
    if data == "exit":
        break

    sock.send(data.encode())


sock.close()
