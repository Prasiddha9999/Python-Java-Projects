
import java.util.Scanner;
public class Area{
public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter length");
    int l1 = sc.nextInt();
    System.out.println("Enter breadth");
    int l2 = sc.nextInt();
    
    area ar = new area(l1, l2);
    System.out.println("The area is " + ar.Aria());
}
}

class area{
    int length;
    int breadth;
    area(int length, int breadth){
    this.length = length;
    this.breadth = breadth;
    }
    int Aria(){
    int A = this.length * this.breadth;
    return A;
    }
}
