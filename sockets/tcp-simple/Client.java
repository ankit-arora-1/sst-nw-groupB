package sockets;

import java.io.IOException;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket();
        socket.connect(new InetSocketAddress("127.0.0.1", 12345));

        socket.getOutputStream().write("hello server".getBytes());


    }
}
