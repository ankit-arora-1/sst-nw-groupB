import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

interface = "127.0.0.1"
port = 12345
sock.bind((interface, port))

data1, addr = sock.recvfrom(1024)
data2, addr = sock.recvfrom(1024)
data3, addr = sock.recvfrom(1024)

print(f"data1 = {data1.decode()}")
print(f"data2 = {data2.decode()}")
print(f"data3 = {data3.decode()}")
