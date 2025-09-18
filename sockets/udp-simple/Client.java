package socketsUDP;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Client {
    public static void main(String[] args) throws IOException {
        // Create UDP socket
        DatagramSocket socket = new DatagramSocket();

        String host = "127.0.0.1";
        int port = 12345;

        // Prepare data to send
        String message = "Hello Server";
        byte[] buffer = message.getBytes();

        // Create packet with destination info
        InetAddress serverAddress = InetAddress.getByName(host);
        DatagramPacket packet = new DatagramPacket(
                buffer,
                buffer.length,
                serverAddress,
                port
        );

        // Send the packet
        socket.send(packet);
        System.out.println("Message sent to server");

        socket.close();
    }
}
