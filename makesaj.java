class Vehicle{
	private String rno, color, type;
{
	
	public Vehicle (Scanner sc) {
        System.out.println("Enter the registeration no. :");
        rno=sc.next();
        System.out.println("Enter the color :");
        color=sc.next();
    }
	public void setType(String type) {
		this.type = type;
	}
	
	public void setFueltype(String fueltype) {
		this.fueltype = fueltype;
	}
	
	public void setCc(int cc) {
		this.cc = cc;
	}
	
	public String getRno() {
		return rno;
	}
	
	public String getColor() {
		return color;
	}
	
	public String getType() {
		return type;
	}
	
	public String getFueltype() {
		return fueltype;
	}
	
	public int getCc() {
		return cc;
	}
}

class Motorcycle extends Vehicle{
	private String fueltype;
	private int cc;
	
	public Motorcycle(Scanner sc) {
		super(sc);
		System.out.println("The vehicle type is: Motorcycle.");
		System.out.println("Enter the fueltype of motorcycle :");
		fueltype = sc.next();
		System.out.println("Enter the cc of motorcycle :");
		cc = sc.nextInt();
		setType("Motorcycle");
		setFueltype(fueltype);
		setCc(cc);
	}
}

class Car extends Vehicle{
	private String fueltype;
	private int cc;
	
	public Car(Scanner sc) {
		super(sc);
		System.out.println("The vehicle type is: Car.");
		System.out.println("Enter the fueltype of car :");
		fueltype = sc.next();
		System.out.println("Enter the cc of car :");
		cc = sc.nextInt();
		setType("Car");
		setFueltype(fueltype);
		setCc(cc);
	}
}

class Truck extends Vehicle{
	private String fueltype;
	private int cc;
	public Truck(Scanner sc) {
		super(sc);
		System.out.println("The vehicle type is: Truck.");
		System.out.println("Enter the fueltype of truck :");
		fueltype = sc.next();
		System.out.println("Enter the cc of truck :");
		cc = sc.nextInt();
	}
}
motorcycle m1=new motorcycle();
        truck t1=new truck();
        car c1=new car()