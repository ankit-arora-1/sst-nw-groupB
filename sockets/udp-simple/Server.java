package socketsUDP;

import java.io.IOException;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        DatagramSocket socket = new DatagramSocket(12345, InetAddress.getByName("127.0.0.1"));
        System.out.println("UDP Server Socket successfully created");
        System.out.println("Socket binded to 12345");
        System.out.println("Socket is listening");

        // Buffer to receive data
        byte[] buffer = new byte[1024];

        while (true) {
            DatagramPacket receivePacket = new DatagramPacket(buffer, buffer.length);

            socket.receive(receivePacket);

            InetAddress clientAddress = receivePacket.getAddress();
            int clientPort = receivePacket.getPort();
            System.out.println("Got packet from " + clientAddress + ":" + clientPort);

            String data = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Received from client: " + data);

            if (data.equalsIgnoreCase("exit")) {
                break;
            }
        }

        socket.close();
    }
}
