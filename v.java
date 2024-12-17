package vivekdsl;

import java.io.*;

import java.net.*;

public class Server {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Server is listening on port 5000...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

                ClientHandler clientHandler = new ClientHandler(clientSocket);
                clientHandler.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class ClientHandler extends Thread {
    private Socket clientSocket;

    public ClientHandler(Socket socket) {
        this.clientSocket = socket;
    }

    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

            
            String input = in.readLine();
            int number = Integer.parseInt(input);

            int square = number * number;
            int cube = number * number * number;

            
            out.println("Square: " + square);
            out.println("Cube: " + cube);

            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


client program

package vivekdsl;
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try {
            Socket clientSocket = new Socket("localhost", 5000);
            System.out.println("Connected to server.");

            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader serverIn = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

            System.out.print("Enter a number: "); 
            String input = in.readLine();

            
            out.println(input);

           
            String squareResponse = serverIn.readLine();
            String cubeResponse = serverIn.readLine();

            System.out.println("Server Response:");
            System.out.println(squareResponse);
            System.out.println(cubeResponse);

            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}