package sockets;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket();
        serverSocket.bind(new InetSocketAddress("127.0.0.1", 12345));
        Socket conn = serverSocket.accept();

        Scanner scanner = new Scanner(conn.getInputStream());


        String data = scanner.nextLine();
        System.out.println(data);

    }
}
