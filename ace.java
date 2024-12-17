import java.util.Scanner;
class vehicle{
	String rno,color,type;
	
}
class motorcycle extends vehicle{
	String fueltype;
	int cc;
	motorcycle(){
		System.out.println("The vehicle type is: Motorcycle.");
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the fueltype of motorcycle :");
		fueltype=sc.next();
		System.out.println("Enter the cc of motorcycle :");
		cc=sc.nextInt();
		System.out.println("Enter the registeration no. :");
		rno=sc.next();
		System.out.println("Enter the colour :");
		color=sc.next();
		
		
	}
}
class car extends vehicle{
	String fueltype;
	int cc;
	car(){
		System.out.println("The vehicle type is: car.");
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the fueltype of car :");
		fueltype=sc.next();
		System.out.println("Enter the cc of car :");
		cc=sc.nextInt();
		System.out.println("Enter the registeration no. :");
		rno=sc.next();
		System.out.println("Enter the colour :");
		color=sc.next();
		
		
	}
}
class truck extends vehicle{
	String fueltype;
	int cc;
	truck(){
		System.out.println("The vehicle type is: truck");
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the fueltype of truck :");
		fueltype=sc.next();
		System.out.println("Enter the cc of truck :");
		cc=sc.nextInt();
		System.out.println("Enter the registeration no. :");
		rno=sc.next();
		System.out.println("Enter the colour :");
		color=sc.next();
		
		
	}
}
public class ace {
	public static void main(String[] args) {
		System.out.println("What Do U Have? :");
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		if (input.equals("motorcycle")) {
			motorcycle m1 = new motorcycle(sc);
		} else if (input.equals("truck")) {
			truck t1 = new truck(sc);
		} else if (input.equals("Car")) {
			car c1 = new car(sc);
		} else {
			System.out.println("No");
		}
	}
}