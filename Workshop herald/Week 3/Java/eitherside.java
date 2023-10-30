import java.util.*;
public class print{
    public static void eitherSide( int a){
    System.out.println("One more is "+ (a+1));
    System.out.println("One less is "+ (a-1));
    }
    public static void main(String[] arg){
        Scanner number = new Scanner(System.in);
        System.out.println("Enter a number");
        int num = number.nextInt();
        eitherSide(num);
        
    }
}