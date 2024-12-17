import java.io.*;
import java.util.*;

public class ac extends Thread {
	public void run()
	{
		System.out.println("Thread Started Running...");
	}
	public static void main(String[] args)
	{
		ac g1 = new ac();
		g1.run();
	}
}
