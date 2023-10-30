import java.util.*;
public class Number{
public static void type(double x){
    System.out.println(x);
    int y = (int)x;
    System.out.println(y);
        }
public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a number");
    double a = sc.nextDouble();
    type(a);

    }
}