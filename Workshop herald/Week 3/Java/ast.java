import java.util.*;
public class printing
{
public static void astric(int a){
    for(int i=0;i<a;i++)
        System.out.println("*");
}
public static void main(String[] arg){
    Scanner number= new Scanner(System.in);
    System.out.print("Enter a number");
    int a = number.nextInt();
    astric(a);
}
}