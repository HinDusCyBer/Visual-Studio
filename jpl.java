import java.util.*;

class Square extends Thread{
    
    int x;
    
    Square(int n){
        x = n;
    }
    
    public void run(){
        
        int sqr = x*x;
        System.out.println("Square of " + x + " = " + sqr);
        
    }
}
class Cube extends Thread{
    
    int x;
    
    Cube(int n){
        x = n;
    }
    
    public void run(){
        
        int cub = x*x*x;
        System.out.println("Cube of " + x + " = " + cub);
        
    }   
}
class Number extends Thread{
    
    public void run() {
        Random random = new Random();
        for(int i =0; i<5; i++)
        {
            
            int randomInteger = random.nextInt(100);
            System.out.println("Random Integer generated : " + randomInteger);
            
            if(randomInteger % 2 == 0) {
                
                System.out.println("Number Generated is Even.");
                
                Square s = new Square(randomInteger);
                s.start();
            }
            
            else {
                
                System.out.println("Number Generated is Odd.");
                
                Cube c = new Cube(randomInteger);
                c.start();
                
            }
        }
    }
}
public class jpl{
    public static void main(String args[]) {
        Number nb = new Number();
        nb.start();
        
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
} 