import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto("hello 1".encode(), ("127.0.0.1", 12345))
sock.sendto("hello 2".encode(), ("127.0.0.1", 12345))
sock.sendto("hello 3".encode(), ("127.0.0.1", 12345))
