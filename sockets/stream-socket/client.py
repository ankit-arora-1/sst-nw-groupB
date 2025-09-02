import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 12345))

sock.send("hello1".encode())
sock.send("hello2".encode())
sock.send("hello3".encode())
