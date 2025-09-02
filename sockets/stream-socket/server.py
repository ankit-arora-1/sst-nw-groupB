import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 12345))
sock.listen()

conn, addr = sock.accept()

data1 = conn.recv(1024)
data2 = conn.recv(1024)
data3 = conn.recv(1024)

print(f"data1 = {data1.decode()}")
print(f"data2 = {data2.decode()}")
print(f"data3 = {data3.decode()}")
