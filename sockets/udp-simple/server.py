import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

interface = "127.0.0.1"
port = 12345
sock.bind((interface, port))

data, addr = sock.recvfrom(1024)
print(f"client = {addr}, data = {data.decode()}")
