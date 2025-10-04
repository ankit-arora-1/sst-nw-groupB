import os
import socket


class SimpleHttpServer:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.resource_dir = "resources"
        self.socket = None

        # check if resources folder is present or not
        # if not present, create it

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)

        print("Server started...")

        while True:
            client_socket, client_address = self.socket.accept()

            self.handle_request(client_socket)

            client_socket.close()

    def handle_request(self, client_socket):
        request_data = client_socket.recv(8096).decode()

        lines = request_data.split("\r\n")

        line = lines[0]
        parts = line.split()

        method = parts[0]
        path = parts[1]

        file_path = os.path.join(self.resource_dir, path)

        # Check if the path is correct and the file exists

        with open(file_path, "r") as f:
            content = f.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Length: 1000\r\n"
            response += "Server: Simple python server\r\n"
            response += "\r\n"
            response += content

            client_socket.send(response)
